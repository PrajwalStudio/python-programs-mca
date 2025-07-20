import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AAPL.csv", parse_dates=True, index_col="Date")

df["20_MA"] = df["Close"].rolling(window=20).mean()

plt.figure(figsize=(10, 5))
plt.plot(df["Close"], label="Close", color="blue")
plt.plot(df["20_MA"], label="20-Day MA", color="orange")
plt.title("AAPL Closing Price with 20-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.show()

monthly_avg = df["Close"].resample("ME").mean()

plt.figure(figsize=(10, 5))
plt.plot(monthly_avg, color="green")
plt.title("AAPL Monthly Average Closing Price")
plt.xlabel("Date")
plt.ylabel("Average Closing Price (USD)")
plt.grid(True)
plt.show()