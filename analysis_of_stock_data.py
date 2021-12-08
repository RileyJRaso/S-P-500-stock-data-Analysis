import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

Date_regex = re.compile('[1-2][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')

def get_Data(filepath):
    data = pd.read_csv(filepath)
    return(data)


def format_Data(data_unformatted):
    data_unformatted.loc[:,'date'] = pd.to_datetime(data_unformatted.loc[:,'date'])
    formatted_data = pd.DataFrame(data_unformatted, columns=['date','close', 'Name'])
    return(formatted_data)


def query_Data_for_stock(data_formatted, stock):
    data_queried = data_formatted.loc[data_formatted.Name == stock,:]
    return data_queried

def Select_years(Stock_data, starting_date, Ending_date):
    Only_wanted_years_data = Stock_data.loc[((Stock_data.date >= starting_date) & (Stock_data.date <= Ending_date)),:]
    return Only_wanted_years_data

def display_Data(Stock_data, x_value, y_value, x_label, y_label, Title):
    plt.plot(Stock_data[x_value], Stock_data[y_value])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(Title)
    plt.show()
    pass

def main():

    stock_data = get_Data(r'./Data/all_stocks_5yr.csv')
    formatted_data = format_Data(stock_data)

    print("What is the symbol of the stock you want to query?")
    stock_symbol = str(input())

    queried_data = query_Data_for_stock(formatted_data, stock_symbol)

    print("What is the start date for the search? (Format YYYY-MM-DD)")
    start_date = str(input())
    while(not(Date_regex.match(start_date)) and start_date >= "2013-02-08"):
        print("it seems the start date entered was in the wrong format or was earlier than dataset, please try again")
        print("(Format YYYY-MM-DD)")
        start_date = str(input())

    print("What is the end date for the search? (Format YYYY-MM-DD)")
    end_date = str(input())
    while(not(Date_regex.match(end_date))):
        print("it seems the end date entered was in the wrong format, please try again")
        print("(Format YYYY-MM-DD)")
        start_date = str(input())

    Only_wanted_years_queried_data = Select_years(queried_data, start_date, end_date)

    print("\nHere is the table for the search\n")
    print(Only_wanted_years_queried_data)

    display_Data(Only_wanted_years_queried_data, 'date', 'close', 'Date', 'Closing Price', ("Stock value for: " + stock_symbol + " between " + start_date + " And " + end_date))

main()
#stock_data = get_Data(r'./Data/all_stocks_5yr.csv')
#formatted_data = format_Data(stock_data)
#queried_data = query_Data_for_stock(formatted_data, 'AAL')
#Only_wanted_years_queried_data = Select_years(queried_data, '2013-02-12', '2013-03-12')
#print(Only_wanted_years_queried_data)
#display_Data(Only_wanted_years_queried_data, 'date', 'close', 'Date', 'Closing Price', ("Stock value for: " + 'AAL' + " between " + '2013-02-12' + " And " + '2013-03-12'))
