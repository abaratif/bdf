import requests
import pandas as pd


GOLD_ID = "8830"
SILVER_ID = "8836"

START_DATE = "07/29/2017"
END_DATE = "08/29/2017"
BASE_URL = "https://www.investing.com/instruments/HistoricalDataAjax"

def scrape(start_date, end_date, commodity_id):
	"""
	Given a a date range and a commodity id,
	scrape historical data from the investing.com site

	Returns a string with the result gotten from the site
	"""
	HEADERS = {
    "X-Requested-With" : "XMLHttpRequest",
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
	}

	data = {
	    "curr_id" : commodity_id,
	    "smlID" : "300004",
	    "st_date" : START_DATE,
	    "end_date" : END_DATE,
	    "interval_sec" : "Daily",
	    "sort_col" : "date",
	    "sort_ord" : "DESC",
	    "action": "historical_data"
	}

	try:
		
		r = requests.post(BASE_URL, data=data, headers=HEADERS)
		assert(r.status_code == 200)
		return r.text

	except Exception as e:
		raise e

	return None

def parse(response_text):
	"""
	Given a string containing HTML response text
	parses out the necessary data
	
	returns a pandas DataFrame object  
	"""
	df = pd.read_html(response_text)
	df = df[0]  # Ignore footer table
	df["Date"] = pd.to_datetime(df["Date"])
	df["Commodity"] = "Gold"

	return df   

response_text = scrape(START_DATE, END_DATE, commodity_id=GOLD_ID)
df = parse(response_text)
df.to_csv()

print(df)