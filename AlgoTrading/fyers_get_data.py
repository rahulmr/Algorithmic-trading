from asyncore import write
from fyers_api import accessToken
from fyers_api import fyersModel
import pandas as pd
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import date
import time
import csv

client_id = "VHPC****HNN-100"                       # Client_id here refers to APP_ID of the created app
op = 0
cl = 0

access_token = open("token.txt", "r").read()

fyers = fyersModel.FyersModel(token=access_token,is_async=False,client_id=client_id,log_path="/Users/upendrasingh/Documents/GitHub/Algorithmic-trading/AlgoTrading/")

def read_csv():
    df = pd.read_csv("StockList.csv")
    timeConvert(df)
    
def fetchData(time_from,time_to,df):
    for row in df.iterrows():
        global name
        name=row[1][0]
        stock="NSE:"+name+"-EQ"
        market_data = fyers.history(
        data = {
        "symbol" : stock,
        "resolution" : "10",
        "date_format" : "1",
        "range_from" : time_from ,
        "range_to" : time_to,
        "cont_flag" : "1"

        }
        )
        val = market_data["candles"]
        fields = ["Date", "Open", "High", "Low" ,"Close", "Volume"]
        
        with open("stock_data_save.csv", "w") as f:
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(val)



def timeConvert(df):
    day = datetime.today() - timedelta(days=3)  #if you want to work on previoius day data
    # day = datetime.now()  #for current day data
    # print("now ->",previous_day)

    format_date = day.strftime("%Y-%m-%d")
    date_time = format_date
    time_from=str(date_time)
    time_to=str(date_time)
    

    fetchData(time_from,time_to,df)


# data = {"symbol":"NSE:SBIN-EQ","resolution":"15","date_format":"1","range_from":"2022-01-28","range_to":"2022-01-28","cont_flag":"1"}
# print(fyers.history(data))


read_csv()