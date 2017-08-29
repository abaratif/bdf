import requests
import pandas as pd
import sys

START_DATE = "07/29/2017"
END_DATE = "08/29/2017"


class Commodity(object):
    """An object that holds price data for a particular commodity,
    across a given date range.
    """
    BASE_URL = "https://www.investing.com/instruments/HistoricalDataAjax"

    def __init__(self, start, end, name):
        self.start = start
        self.end = end
        self.name = name
        self.response = self.scrape()

    def scrape(self):
        """
        Given a Commodity object with a date range and a commodity id,
        scrape historical data from the investing.com site

        Stores a string with the result gotten from the site
        """
        HEADERS = {
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
        }

        ID_MAPPING = {
            "gold": "8830",
            "silver": "8836"
        }

        data = {
            "curr_id": ID_MAPPING[self.name],
            "smlID": "300004",
            "st_date": self.start,
            "end_date": self.end,
            "interval_sec": "Daily",
            "sort_col": "date",
            "sort_ord": "DESC",
            "action": "historical_data"
        }

        try:
            r = requests.post(self.BASE_URL, data=data, headers=HEADERS)
            assert(r.status_code == 200)
            return r.text
        except Exception as e:
            raise e

    def to_df(self):
        """
        returns a pandas DataFrame object based on parsed data from a
        Commodity object's HTML
        """
        df = pd.read_html(self.response)
        df = df[0]  # Ignore footer table
        df["Date"] = pd.to_datetime(df["Date"])
        df["Commodity"] = self.name

        return df

if __name__ == '__main__':
    OUTPUT_FILE = sys.argv[1]

    gold = Commodity(START_DATE, END_DATE, "gold").to_df()
    silver = Commodity(START_DATE, END_DATE, "silver").to_df()

    combined = gold.append(silver)
    combined.index.name = 'index'
    combined.to_csv(OUTPUT_FILE)
