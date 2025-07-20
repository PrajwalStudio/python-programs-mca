import pandas as pd
from datetime import date, datetime
import pytz

# Load and parse the CSV time series data
df = pd.read_csv('AAPL.csv', parse_dates=True, index_col="Date")

# Monthly average of 'Close' prices
monthly_avg = df['Close'].resample('ME').mean()
print("Monthly average closing prices:\n", monthly_avg.head())

# Mean closing price for October 2014
oct_avg = df.loc['2014-10'].Close.mean()
print("\nAverage closing price in October 2014:", oct_avg)

# Display current date and time in Asia/Kolkata timezone
now = datetime.now(pytz.timezone('Asia/Kolkata'))
print("\nCurrent Date and Time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)

# Function to find number of days between two dates
def numOfDays(date1, date2):
    return (date2 - date1).days

# Example usage: days since 30 Sep 2000
date1 = date(2000, 9, 30)
date2 = date.today()
print("\nDays since you were born:", numOfDays(date1, date2))
