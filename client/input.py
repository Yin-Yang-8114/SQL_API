import questionary

def validate_id(value):
    try:
        number = int(value)
    except ValueError:
        return "Enter a whole number"
    if number <= 0:
        return "The number must be greater than zero"
    return True

def validate_text(value):
    if not value.strip():
        return "This field cannot be empty"
    return True


def choose_search(text_field="name"):
    return questionary.select("Search by:",choices=[questionary.Choice("ID", value="id"),questionary.Choice(text_field, value=text_field), ],).unsafe_ask()


def read_id():
    value = questionary.text("Enter ID:",validate=validate_id,).unsafe_ask()
    return int(value)

def choose_action():
    return questionary.select(
        "Choose an action:",
        choices=[
            questionary.Choice("Search", value="search"),
            questionary.Choice("Register", value="register"),
            questionary.Choice("Secure search", value="secure_search"),
            questionary.Choice("Exit", value="exit"),
        ],
    ).unsafe_ask()
def read_credentials():
    username = read_text("Enter username:")
    password = questionary.password(
        "Enter password:",
        validate=validate_text,
    ).unsafe_ask()
    return {
        "username": username,
        "password": password,}


def read_search_params():
    search_type = choose_search("name")
    if search_type == "id":
        return {"device_id": read_id()}
    return {"device_name": read_text("Enter device name:")}

def read_text(message="Enter name:"):
    value = questionary.text(message,validate=validate_text,).unsafe_ask()
    return value.strip()