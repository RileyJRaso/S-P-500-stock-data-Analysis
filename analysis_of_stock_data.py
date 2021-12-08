import pandas as pd
import numpy as np

def get_Data(filepath):
    data = pd.read_csv(filepath)
    return(data)


def clean_Data(data_uncleaned):
    data_uncleaned.loc[:,'date'] = pd.to_datetime(data_uncleaned.loc[:,'date'])
    cleaned_data = pd.DataFrame(data_uncleaned, columns=['date','close', 'Name'])
    return(cleaned_data)


def query_Data_for_stock(data_cleaned, stock):
    data_queried = data_cleaned.loc[data_cleaned.Name == stock,:]
    return data_queried

def Select_years(Stock_data, starting_date, Ending_date):
    return Stock_data

def display_Data():
    pass


stock_data = get_Data(r'./Data/all_stocks_5yr.csv')
cleaned_data = clean_Data_only_close(stock_data)
queried_data = query_Data_for_stock(cleaned_data, 'AAL')
cleaned_queried_data = Select_years(queried_data, '2013-02-12', '2014-03-12')
print(cleaned_queried_data.dtypes)
