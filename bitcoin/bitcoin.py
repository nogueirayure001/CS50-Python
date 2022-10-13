import requests
from sys import exit, argv

API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    if len(argv) == 1:
        exit('Missing command-line argument')

    try:
        quantity = float(argv[1])
    except ValueError:
        exit('Command-line argument is not a number')

    price = get_bitcoin_rate() * quantity
    print(f'${price:,.4f}')


def get_bitcoin_rate():
    response = requests.get(API_URL).json()
    return response['bpi']['USD']['rate_float']


if __name__ == '__main__':
    main()
