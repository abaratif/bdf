import pandas as pd
import sys

if __name__ == '__main__':
    START_DATE = sys.argv[1]
    END_DATE = sys.argv[2]
    COMMODITY_NAME = sys.argv[3]

    CSV_PATH = 'data.csv'

    df = pd.read_csv(CSV_PATH, index_col='index')

    filtered = df[
        (df.Date >= START_DATE) &
        (df.Date <= END_DATE) &
        (df.Commodity == COMMODITY_NAME)
        ]

    mean = format(filtered['Price'].mean(), '.2f')
    var = format(filtered['Price'].var(ddof=0), '.2f')  # Population variance

    print("{} {} {}".format(COMMODITY_NAME, mean, var))
