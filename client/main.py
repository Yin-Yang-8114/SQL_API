import requests
from SQL_API.client.input import choose_action, read_credentials, read_search_params
from SQL_API.client.api import get_data, post_data
from SQL_API.client.output import show_result, show_error, show_message

def run_register():
    data = read_credentials()
    result = post_data("/register", data)
    show_message(result["message"])

def run_search(secure):
    if secure:
        data = read_credentials()
        params = read_search_params()
        data.update(params)
        result = post_data(
            "/devices/lowest-readiness/secure",
            data,)
    else:
        params = read_search_params()
        result = get_data("/devices/lowest-readiness", params)

    show_result(result)


def main():
    while True:
        try:
            action = choose_action()

            if action == "exit":
                break
            if action == "register":
                run_register()
            elif action == "search":
                run_search(False)
            elif action == "secure_search":
                run_search(True)
        except requests.exceptions.HTTPError as error:
            try:
                message = error.response.json().get("detail", str(error))
            except ValueError:
                message = str(error)
            show_error(message)
        except requests.exceptions.RequestException as error:
            show_error(str(error))

        except (KeyboardInterrupt, EOFError):
            break


if __name__ == "__main__":
    main()