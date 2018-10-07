import pandas as pd
pd.core.common.is_list_like= pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime

stock1=input("enter stock1 symbol(example: AMZN)") #user input
time1=[int(x) for x in input("maximum interval for analysis is six months,enter the start time: year moth date(example: 2008 6 1)",).split()]
time2=[int(x) for x in input("enter the end time,: year moth date(example: 2009 3 31)",).split()]
start_date=datetime.datetime(*time1)
end_date=datetime.datetime(*time2)

def get_price_history(stock_symbol,start_date,end_date):
    dff = web.DataReader(stock_symbol, 'quandl', start_date, end_date) #use quandl, yahoo and google do not work
    dff.reset_index(inplace=True)
    dff.set_index("Date", inplace=True)
    dff["of_first_value"]=dff["AdjClose"]/dff.iloc[-1]["AdjClose"]*100 #add a column
    return dff

df=get_price_history(stock1,start_date,end_date)
table_name=stock1
conn ='sqlite:///full_stock_data2.db'#database name
df.to_sql(table_name, conn, if_exists='append', index=True)
