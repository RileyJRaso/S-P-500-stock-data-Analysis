import pandas as pd
import numpy as np

def get_Data(filepath):
    data = pd.read_csv(filepath)
    return(data)


def clean_Data():
    pass


def sort_Data():
    pass


def display_Data():
    pass


stack_data = get_Data(r'./Data/all_stocks_5yr.csv')
