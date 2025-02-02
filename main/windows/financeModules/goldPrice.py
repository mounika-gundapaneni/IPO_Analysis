import requests
import json
from datetime import datetime, timedelta

# Define the API endpoints and keys
GOLD_API_URL = "https://www.goldapi.io/dashboard"
GOLD_API_KEY = "goldapi-3q7v1ysm6mzmzhk-io"
HOUSE_API_URL = "https://api.example.com/house_prices"  # Replace with actual house price API
HOUSE_API_KEY = "your_house_api_key_here"

# Function to fetch historical gold prices
def fetch_gold_prices(start_date, end_date):
    params = {
        "access_key": GOLD_API_KEY,
        "start_date": start_date,
        "end_date": end_date,
        "base": "USD",
        "symbols": "XAU"
    }
    response = requests.get(GOLD_API_URL, params=params)
    response.raise_for_status()
    return response.json()

# Function to fetch historical house prices
def fetch_house_prices(start_date, end_date):
    params = {
        "api_key": HOUSE_API_KEY,
        "start_date": start_date,
        "end_date": end_date
    }
    response = requests.get(HOUSE_API_URL, params=params)
    response.raise_for_status()
    return response.json()

# Function to compare gold and house prices
def compare_prices(gold_data, house_data):
    comparison = []
    for date in gold_data["rates"]:
        gold_price = gold_data["rates"][date]["XAU"]
        house_price = house_data["prices"].get(date, None)
        if house_price:
            comparison.append({
                "date": date,
                "gold_price": gold_price,
                "house_price": house_price
            })
    return comparison

if __name__ == "__main__":
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=365*10)).strftime("%Y-%m-%d")

    gold_data = fetch_gold_prices(start_date, end_date)
    house_data = fetch_house_prices(start_date, end_date)

    comparison = compare_prices(gold_data, house_data)
    print(json.dumps(comparison, indent=4))
