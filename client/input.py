import questionary

def choose_search_type(text_field="name"):
    return questionary.select("Search by:",choices=[questionary.Choice("ID", value="id"),questionary.Choice(text_field, value=text_field), ],).unsafe_ask()

def read_target_id():
    valid = True
    while valid:
        value = questionary.text("Enter ID:").ask()
        try:
            number = int(value)
            if number <= 0:
                print("The number must be greater than zero")
            else:
                valid = False
        except ValueError:
            print("Enter a whole number")
    return value

def read_target_name():
    valid = True
    while valid:
        value = questionary.text("Enter name:").ask()
        if not value.strip():
            print( "This field cannot be empty")
        else:
            valid = False
    return value