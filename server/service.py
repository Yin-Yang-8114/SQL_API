from SQL_API.server.database import db

def find_lowest_readiness(search_type, search_value):
    if search_type == "id":
        condition = "d.id = %s"
    elif search_type == "name":
        condition = "d.name = %s"
    else:
        raise ValueError("Search type must be id or name")

    query = f"""
        SELECT
            d.id,
            d.name,
            s.name,
            s.city,
            ds.total_units,
            ds.operational_units,
            ds.operational_units * 100.0 / ds.total_units
                AS readiness_percent
        FROM communication_devices AS d
        JOIN device_status AS ds
            ON d.id = ds.device_id
        JOIN communication_stations AS s
            ON s.id = ds.station_id
        WHERE {condition}
            AND s.is_active = 1
            AND ds.total_units > 0
        ORDER BY readiness_percent ASC, s.id ASC
        LIMIT 1
    """
    with db.connection_context():
        cursor = db.execute_sql(query, (search_value,))
        row = cursor.fetchone()
    if row is None:
        return None
    result = {
        "device_id": row[0],
        "device_name": row[1],
        "station_name": row[2],
        "city": row[3],
        "total_units": row[4],
        "operational_units": row[5],
        "readiness_percent": round(float(row[6]), 2),}
    return result