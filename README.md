# bdf

Scripts to scrape price data from investing.com and to run a simple query.

## Running

### Setup

These scripts depend on the python packages pandas and requests. The best way to install them in using a python virtual environment.

```
python3 -m venv VENV
source VENV/bin/activate
pip install -r requirements.txt
```

### Scraping Data

Run the scrape.py script, and specify a target output filename as a runtime argument. The scrape script scrapes data for both gold and silver, and other settings such as date range are stored in variables that can easily be edited.

```
python scrape.py data.csv
```

### Running Analysis

## Writeup

### Scraping

#### Formulating the Request

I initially began by looking at the investing.com website in the Chrome inspector. While watching the network tab, I noticed that a jQuery script in the page would make a request to the URL ```https://www.investing.com/instruments/HistoricalDataAjax``` every time I would change the date parameters of the table. I checked out the headers and form data for request, and used Postman to reproduce the request. I had to play around with some of the particulars of the headers, and eventually got back an HTML response similar to the one I had observed in the Chrome inspector. Once I had the request structure figured out for one commodity, I tried the other and observed the change in the ```curr_id``` field in the form data. I recorded these two and wrote up a function to encapsulate all of this logic.

#### Parsing the HTML

I initially thought of using different libraries to try and parse out the particular section of the HTML that I would need, but later realized that the pandas library would be able to accomplish this for me, since the data was already in a tabular format. I wrote a new function to parse the data into a pandas DataFrame, and added some additional functionality to store the dates properly, and to add the name of the commodity as a column in the DataFrame.

#### Code Cleanup

At this point, the code was getting sort of spaghetti-like, so I took a moment to re-organize everything into a single object, and to abstract out constants into easy to change variables.

### Analysis
