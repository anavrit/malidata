import numpy as np
import pandas as pd
import os

def clean_string(data, list_of_col):
    for col in list_of_col:
        data[col] = data[col].str.upper()
        data[col] = data[col].str.strip()
    return data

def replace_values(data, list_of_col, list_dict_of_values):
    for i, col in enumerate(list_of_col):
        for key, val in list_dict_of_values[i].items():
            data.loc[data[col] == key, col] = val
    return data

def append_categories(data, dict_to_append):
    for key, val in dict_to_append.items():
        data.loc['ID'] = key
        data.loc[data['ID'] == key, 'CATEGORIES'] = val
        data.reset_index(inplace=True)
        data.drop('index', axis=1, inplace=True)
    return data

def create_category_csv(df, col):
    newdict = {}
    for i, ind in enumerate(list(df[col].value_counts().index)):
        newdict[i+1] = ind
    data = pd.DataFrame(newdict.items(), columns=['ID', 'CATEGORIES'])
    return data

def convert_to_numerical_category(df1, df2, list_of_col):
    for col in list_of_col:
        df1 = df1.merge(df2, left_on=col, right_on='CATEGORIES', how='left')
        df1 = df1.drop(['CATEGORIES', col], axis=1)
        df1 = df1.rename(columns={'ID': col})
    return df1

def load_category_csv(col):
    q = pd.read_csv(f'data/herams_{col}_categories.csv')
    q.index += 1
    q.reset_index(inplace=True)
    q = q.rename(columns={'index': 'ID'})
    return q
