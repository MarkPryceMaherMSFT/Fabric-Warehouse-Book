"""Runnable Fabric Spark notebook template; refreshes selected endpoint metadata.

Requires BookLakehouse (schema-enabled) as the notebook's default Lakehouse,
the seeded book schema, semantic-link/sempy, and Contributor or higher access.
No source Delta data is written. Endpoint metadata is refreshed. Failures raise.

Adapted with user authorization from Mark Pryce-Maher,
MDSync-Sync-selected-tables.py, substantive revision 16 August 2026:
Canonical: https://gist.github.com/MarkPryceMaherMSFT/190fa079d89a2f301af2847583d5d757
Pinned revision:
https://gist.github.com/MarkPryceMaherMSFT/190fa079d89a2f301af2847583d5d757/ae4988bf8c833ca581cd1fe8071855bdddebfb47
No explicit license was identified on the source gist.
Changes: one discovery GET; nonempty/limited selection; no nonexistent table;
no swallowed exceptions; strict complete per-table success validation; no reset.
9 November 2026 update: require successful endpoint provisioning before POST.
REST contracts rechecked 9 November 2026; no tenant execution:
https://learn.microsoft.com/en-us/rest/api/fabric/sqlendpoint/items/refresh-sql-endpoint-metadata
https://learn.microsoft.com/en-us/rest/api/fabric/lakehouse/items/get-lakehouse
"""

from uuid import UUID


TABLES = [{"schema": "book", "tableNames": ["DimCustomer", "FactSales"]}]


def selected_names(tables):
    """Validate before POST: an empty selection would refresh the whole item."""
    if not isinstance(tables, list) or not tables:
        raise ValueError("Select between 1 and 25 tables; empty means all in the API.")
    names = []
    for group in tables:
        if not isinstance(group, dict):
            raise ValueError("Every table group must be a dictionary.")
        schema = group.get("schema")
        table_names = group.get("tableNames")
        if not isinstance(schema, str) or not schema.strip() or len(schema) > 128:
            raise ValueError("Supply a nonempty schema name of at most 128 characters.")
        if not isinstance(table_names, list) or not table_names:
            raise ValueError("Every schema group requires a nonempty tableNames list.")
        for table in table_names:
            if not isinstance(table, str) or not table.strip() or len(table) > 128:
                raise ValueError("Supply nonempty table names of at most 128 characters.")
            # The documented response identifies schema-enabled tables as schema.table.
            if "." in schema or "." in table:
                raise ValueError("This template excludes dotted identifiers.")
            names.append(f"{schema}.{table}")
    if len(names) > 25 or len(set(names)) != len(names):
        raise ValueError("Select at most 25 distinct schema-qualified tables.")
    return set(names)


def validate_table_results(payload, expected):
    """Reject partial success, missing tables, unknown states, and bad payloads."""
    if not isinstance(payload, dict) or not isinstance(payload.get("value"), list):
        raise RuntimeError("Refresh returned no documented per-table result list.")
    observed = set()
    failures = []
    for row in payload["value"]:
        if not isinstance(row, dict):
            failures.append("Malformed table result")
            continue
        name = row.get("tableName")
        status = row.get("status")
        if not isinstance(name, str):
            failures.append("Table result has no valid tableName")
            continue
        if name in observed:
            failures.append(f"{name}: duplicate result")
        observed.add(name)
        if name not in expected:
            failures.append(f"{name}: unexpected result")
        if status != "Success":
            error = row.get("error")
            code = error.get("errorCode", "no error code") if isinstance(error, dict) else "no error code"
            failures.append(f"{name}: {status!r} ({code})")
    failures.extend(f"{name}: missing result" for name in sorted(expected - observed))
    if failures:
        raise RuntimeError("Selected-table refresh incomplete: " + "; ".join(failures))
    return payload["value"]


def refresh_selected_tables(spark_session, tables):
    import sempy.fabric as fabric

    expected = selected_names(tables)
    workspace_id = str(UUID(spark_session.conf.get("trident.workspace.id")))
    lakehouse_id = str(UUID(spark_session.conf.get("trident.lakehouse.id")))
    client = fabric.FabricRestClient()

    discovery = client.get(
        f"/v1/workspaces/{workspace_id}/lakehouses/{lakehouse_id}"
    )
    discovery.raise_for_status()
    item = discovery.json()
    endpoint = item.get("properties", {}).get("sqlEndpointProperties", {})
    endpoint_id = endpoint.get("id")
    if not endpoint_id:
        raise RuntimeError("Default Lakehouse has no discoverable SQL endpoint ID.")
    endpoint_id = str(UUID(endpoint_id))
    if item.get("displayName") != "BookLakehouse":
        raise RuntimeError("Default Lakehouse must be BookLakehouse for this template.")
    provisioning_status = endpoint.get("provisioningStatus")
    if provisioning_status != "Success":
        raise RuntimeError(
            "SQL endpoint provisioning must be 'Success' before refresh; "
            f"got {provisioning_status!r}. No refresh was submitted."
        )

    response = client.post(
        f"/v1/workspaces/{workspace_id}/sqlEndpoints/{endpoint_id}/refreshMetadata",
        json={
            "tables": tables,
            "recreateTables": False,
            "timeout": {"timeUnit": "Minutes", "value": 10},
        },
        lro_wait=True,
    )
    response.raise_for_status()
    if response.status_code != 200:
        raise RuntimeError(
            "No completed 200 response; inspect the LRO instead of assuming success."
        )
    rows = validate_table_results(response.json(), expected)
    for row in rows:
        print(
            row["tableName"],
            row["status"],
            row.get("lastSuccessfulSyncDateTime", "timestamp not returned"),
        )
    return rows


def main():
    from pyspark.sql import SparkSession

    session = SparkSession.getActiveSession()
    if session is None:
        raise RuntimeError("Run inside a Fabric Spark notebook with BookLakehouse attached.")
    refresh_selected_tables(session, TABLES)


if __name__ == "__main__":
    main()
