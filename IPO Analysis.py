import requests
import json

# Finhub API key
API_KEY = "cts40dpr01qh9oes8pmgcts40dpr01qh9oes8pn0"

# Define the API endpoint and parameters
url = "https://finnhub.io/api/v1/calendar/ipo"
params = {
    "from": "2024-12-01",
    "to": "2024-12-31",
    "token": API_KEY
}

# Fetch the data
response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

# Keywords to filter the 'name' column
keywords = [
    "Holding", "Holdings","HOLDING", "HOLDINGS", "Venture", "ACQUISITION", "Acquisition", "Biotechnology",
    "Bio", "BIOMEDICAL", "BIOMATERIALS", "Capital", "Investment"
]

# Filter rows
filtered_data = [
    entry for entry in data.get("ipoCalendar", [])
    if not any(keyword in entry.get("name", "") for keyword in keywords)
]

# Write filtered data to a JSON file
output_file = "filtered_ipo_calendar12.json"
with open(output_file, "w") as f:
    json.dump(filtered_data, f, indent=4)

print(f"Filtered data has been written to {output_file}")
