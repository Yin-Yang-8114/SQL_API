import requests
from target_search import choose_search_type, read_target_id, read_target_name
from http_client import request_last_location
from output import show_last_location


def main():
    while True:
        try:
            search_type = choose_search_type()
            if search_type == "id":
                search_value = read_target_id()
            else:
                search_value = read_target_name()
            result = request_last_location(search_type, search_value)
            show_last_location(result)
        except requests.exceptions.HTTPError as error:
            try:
                message = error.response.json().get("detail", str(error))
            except ValueError:
                message = str(error)
            print(f"Error: {message}")
        except requests.exceptions.RequestException as error:
            print(f"Connection error: {error}")
        except (KeyboardInterrupt, EOFError):
            break


def accepted_tp_cyber():
    while True:
        answer=input('did I got accepted to cyber? ')
        if answer.strip().lower() == 'yes':
            main()
        else:
            print('wrong answer try again')
if __name__ == "__main__":
    accepted_tp_cyber()

