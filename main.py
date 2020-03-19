import requests


def main():
    try:
        response = requests.get("https://vasiliev.codes")
        response.raise_for_status()
        print(response.content)
    except Exception as err:
        print(str(err))


if __name__ == "__main__":
    main()
