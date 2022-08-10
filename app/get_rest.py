import requests
import json


def main():

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(response.status_code)
    json_raw = response.json()
    json_formed = json.dumps(json_raw, sort_keys=True, indent=4)
    print(json_formed)
    bpi = json_raw['bpi']
    for ccy in bpi:
        print('Iterating:')
        #print(ccy)
        b_c = bpi[ccy]
        print(b_c['symbol'])


if __name__ == "__main__":
    main()
