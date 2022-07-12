import requests


def main():

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    main()
