from db import db


def find_last_location(search_type, search_value):
    if search_type == "id":
        condition = "t.id = %s"
    elif search_type == "name":
        condition = "t.name = %s"
    else:
        raise ValueError("Search type must be id or name")

    query = f"""
        SELECT
            t.id,
            t.name,
            l.name,
            l.country,
            l.description
        FROM targets AS t
        JOIN locations AS l
            ON t.last_known_location_id = l.id
        WHERE {condition}
        LIMIT 1
    """
    with db.connection_context():
        cursor = db.execute_sql(query, (search_value,))
        row = cursor.fetchone()
    if row is None:
        return None
    return {
        "target_id": row[0],
        "target_name": row[1],
        "location_name": row[2],
        "country": row[3],
        "description": row[4],}
