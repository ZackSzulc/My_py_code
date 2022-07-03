import requests
import sys
import json


def main():
    try:
        sys.argv[1] = float(sys.argv[1])
    except IndexError:
        sys.exit("Not enough arguements.")
    except ValueError:
        sys.exit("Wrong type of information. Must be a float")

    bcoin_rate = get_btc()
    total = round(sys.argv[1]*bcoin_rate, 4)

#had to look this command up :(
    print(f"${total:,.4f}")


def get_btc():
    try:
        bcoin_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bcoin_data = bcoin_data.json()
        return bcoin_data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit()

main()