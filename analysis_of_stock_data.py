import pandas as pd
import numpy as np

def get_Data(filepath):
    data = pd.read_csv(filepath)
    return(data)


def clean_Data_only_close(data_uncleaned):
    cleaned_data = pd.DataFrame(data_uncleaned, columns=['date','close', 'Name'])
    return(cleaned_data)


def query_Data_for_stock(data_cleaned, stock):
    data_queried = data_cleaned.loc[data_cleaned.Name == stock,:]
    return data_queried

def display_Data():
    pass


stock_data = get_Data(r'./Data/all_stocks_5yr.csv')
cleaned_data = clean_Data_only_close(stock_data)
queried_data = query_Data_for_stock(cleaned_data, 'AAL')
print(queried_data)
