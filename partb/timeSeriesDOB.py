import pandas as pd
from datetime import date, datetime
import pytz

df = pd.read_csv('AAPL.csv', parse_dates=True, index_col="Date")

monthly_avg = df['Close'].resample('ME').mean()
print("Monthly average closing prices:\n", monthly_avg.head())

oct_avg = df.loc['2014-10'].Close.mean()
print("\nAverage closing price in October 2014:", oct_avg)

now = datetime.now(pytz.timezone('Asia/Kolkata'))
print("\nCurrent Date and Time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)

def numOfDays(date1, date2):
    return (date2 - date1).days

date1 = date(2003, 12, 17)
date2 = date.today()
print("\nDays since you were born:", numOfDays(date1, date2))


'''import pandas as pd
from datetime import date

df = pd.read_csv('AAPL.csv', index_col="Date", parse_dates=True)

# Monthly average closing prices
monthly_avg = df['Close'].resample('M').mean()
print("Monthly average closing prices:\n", monthly_avg.head())

# Average closing price in October 2014
oct_avg = df.loc['2014-10'].Close.mean()
print("\nAverage closing price in October 2014:", oct_avg)

# Days since birth
def numOfDays(date1, date2):
    return (date2 - date1).days

date1 = date(2003, 12, 17)
date2 = date.today()
print("\nDays since you were born:", numOfDays(date1, date2))
'''