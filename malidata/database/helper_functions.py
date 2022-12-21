import pandas as pd
import numpy as np
import os

def convert_to_csv(names_array, colname, filename):
    names = pd.Series(names_array).to_frame()
    names.reset_index(inplace=True)
    names = names.rename(columns = {0: colname})
    names.drop('index', axis=1, inplace=True)
    names.sort_values(colname, axis=0, inplace=True)
    names.to_csv(f"data/{filename}.csv", index = False)
    return names

def merge_columns(df1, df2, left_on_list, right_on_list, drop_list):
    temp = df1.merge(df2, left_on=left_on_list, right_on=right_on_list)
    assert temp.shape[0] == df1.shape[0]
    temp.drop(drop_list, axis=1, inplace=True)
    return temp

"""
def replace_values(df, list_of_col, list_of_tuple_values):
    for col in list_of_col:
        for old, new in list_of_tuple_values:
            df[col] = df[col].replace([old], new)
    return df
"""

def clean_strings(df, list_of_col):
    for col in list_of_col:
        df[col] = df[col].str.upper()
        df[col] = df[col].str.rstrip()
    return df

def get_serial_column(df, list_of_col, serial):
    df = df.reset_index().reset_index()
    df = df.sort_values(by=list_of_col, axis=0)
    df = df.drop('index', axis=1)
    df = df.rename(columns = {'level_0': serial})
    df[serial] += 1
    return df
