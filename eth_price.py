import requests

def get_eth_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
    data = response.json()
    print("Ethereum price in USD:", data['ethereum']['usd'])

if __name__ == "__main__":
    get_eth_price()
