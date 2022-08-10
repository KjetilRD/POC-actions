import requests
import json


def main():

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(response.status_code)
    json_raw = response.json()
    json_formed = json.dumps(json_raw, sort_keys=True, indent=4)
    print(json_formed)
    for ccy in json_formed:
        print('Iterating:')
        print(ccy)

if __name__ == "__main__":
    main()
