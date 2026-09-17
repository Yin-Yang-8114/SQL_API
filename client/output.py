
""""
Target ID: <target_id> 
Target name: <target_name> 
Last known location: <location_name> 
Country: <country> 
Description: <description>
"""

def show_last_location(result: dict):
    print(f"Target ID: {result['target_id']}")
    print(f"Target name: {result['target_name']}")
    print(f"Last known location: {result['location_name']}")
    print(f"Country: {result['country']}")
    print(f"Description: {result['description']}")
