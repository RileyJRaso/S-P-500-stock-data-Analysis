import pandas as pd
import numpy as np

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

def display_Data():
    pass


stock_data = get_Data(r'./Data/all_stocks_5yr.csv')
formatted_data = format_Data(stock_data)
queried_data = query_Data_for_stock(formatted_data, 'AAL')
Only_wanted_years_queried_data = Select_years(queried_data, '2013-02-12', '2013-03-12')
print(Only_wanted_years_queried_data)
