import requests
import os, sys
import json
from datetime import datetime, timedelta
import configparser

from financeModules.ipo_analysis import *


all_output_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'Results')

#----------------- IPOs Analysis, Finnhub Keys and Results folder Setup -----------------
keys_file= os.path.join(os.path.dirname(__file__), '..', '..', 'keys', 'keys.properties')
config = configparser.ConfigParser()
config.read(keys_file)
finnhub_api_key = config.get("API_KEYS","finnhub-api-key")
print(f"finnhub_api_key: {finnhub_api_key}")
# IPOs_Results Folder Setup
ipoResults_folder = os.path.join(all_output_folder, 'IPOs_List')
input_year = 2024
generate_monthly_iposList(finnhub_api_key, input_year, ipoResults_folder)






