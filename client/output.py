def show_result(result):
    print("")
    print(f"Device ID: {result['device_id']}")
    print(f"Device name: {result['device_name']}")
    print(f"Station: {result['station_name']}")
    print(f"City: {result['city']}")
    print(f"Total units: {result['total_units']}")
    print(f"Operational units: {result['operational_units']}")
    print(f"Readiness: {result['readiness_percent']}%")


def show_error(message):
    print(f"Error: {message}")

def show_message(message):
    print(message)