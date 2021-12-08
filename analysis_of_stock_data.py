import pandas as pd
import numpy as np

def get_Data(filepath):
    data = pd.read_csv(filepath)
    return(data)


def clean_Data_only_close(data_uncleaned):
    cleaned_data = pd.DataFrame(data_uncleaned, columns=['date','close', 'Name'])
    return(cleaned_data)


def sort_Data():
    pass


def display_Data():
    pass


stock_data = get_Data(r'./Data/all_stocks_5yr.csv')
cleaned_data = clean_Data_only_close(stock_data)
print(cleaned_data)
