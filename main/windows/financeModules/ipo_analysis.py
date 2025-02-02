import requests
import os, sys
import json
from datetime import datetime, timedelta
import configparser


# Define the API endpoint
url = "https://finnhub.io/api/v1/calendar/ipo"

# Keywords to filter the 'name' column
filterOut_keywords = [
        "Holding", "Holdings", "HOLDING", "HOLDINGS", "Venture", "ACQUISITION", "Acquisition", "Biotechnology",
        "Bio", "BIOMEDICAL", "BIOMATERIALS", "Capital", "Investment"
]

# Function to generate the parameters for each month in a year
def generate_monthly_dates(key, year):
    dates_list = []
    for month in range(1, 13):
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            end_date = datetime(year, month + 1, 1) - timedelta(days=1)
        dates_list.append({
            "from": start_date.strftime("%Y-%m-%d"),
            "to": end_date.strftime("%Y-%m-%d"),
            "token": key
        })
    return dates_list

# Iterate over each month's parameters
def generate_monthly_iposList(key, year, results_folder):
    
    curr_output_folder = os.path.join(results_folder, str(year))
    if not os.path.exists(curr_output_folder):
        os.makedirs(curr_output_folder)

    monthly_dates = generate_monthly_dates(key, year)
    
    for params in monthly_dates:
        # Fetch the data
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Filter rows
        filtered_data = [
            entry for entry in data.get("ipoCalendar", [])
            if not any(keyword in entry.get("name", "") for keyword in filterOut_keywords)
        ]

        # Write filtered data to a JSON file
        output_file = os.path.join(curr_output_folder, f"filtered_ipo_calendar_{params['from'][:7]}.json")
        with open(output_file, "w") as f:
            json.dump(filtered_data, f, indent=4)

        print(f"Filtered data for {params['from'][:7]} has been written to {output_file}")
    
