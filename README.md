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

### Scraping data

Run the scrape.py script, and specify a target output filename as a runtime argument. The scrape script scrapes data for both gold and silver, and other settings such as date range are stored in variables that can easily be edited.

```
python scrape.py data.csv
```
