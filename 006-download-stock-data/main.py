import requests
from datetime import datetime
import time

ticker = input("Enger ticker symbol:")
from_date = input("Enter start date in yyy/mm/dd format:")
to_date = input("Enter end date in yyy/mm/dd format:")

# Change time to second format
from_datetime = datetime.strptime(from_date, "%Y/%m/%d")
to_datetime = datetime.strptime(to_date, "%Y/%m/%d")
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

# Impersonates browser (otherwise will not be allowed to download data)
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

# Could use .text and then below "w" instead, but this allows to download other kinds of files too (binary and nonbinary files)
content = requests.get(url, headers=headers).content
print(content)

with open("data.csv", "wb") as file:
    file.write(content)