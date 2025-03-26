#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Provides additional pandas functions for interacting with a dataframe object. 
Adhere to the followin instructions to get the most out of the module:
1. Pass your style functions into one of the following methods:
    Styler.applymap: elementwise
    Styler.apply: column-/row-/table-wise
  For columnwise use axis=0, rowwise use axis=1
2. Note that you can chain commands, e.g.,
    df.style.\
        applymap(color_negative_red).\
        apply(highlight_max)
3. To access particular columns, use IndexSlice, e.g., 
    df.style.applymap(color_negative_vals,
                  subset=pd.IndexSlice[2:5, ['B', 'D']])
"""

import seaborn as sns   # 3rd party packages
import pandas as pd
import numpy as np
import matplotlib.pyplot 

__author__ = "Vince J. Straub"

def main():
    pass

def summary_info(df):
    """AIM -> Provide summary info.
    INPUT  -> df.
    OUTPUT -> shape, info, describe."""
    cols = list(df.columns)
    print('\n\n Dimensionaltiy\n')
    display(df.shape)
    print('\n\n Summary data types info')
    display(df.describe(include = 'all'))
    print('\n\n Summary of all columns when the dataframe has mixed column types\n')
    display(df.describe(include = 'all'))

def drop_multiple_col(col_names_list, df): 
    """AIM -> Drop multiple columns based on their column names.
    INPUT -> List of column names, df.
    OUTPUT -> updated df with dropped columns"""
    df.drop(col_names_list, axis=1, inplace=True)
    return df

def all_object_to_numeric(df): 
    """AIM-> Changing dtypes to save memory
    INPUT  -> df.
    OUTPUT -> updated df with numeric columns"""
    cols = df.columns[df.dtypes.eq('object')]
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

def check_missing_data(df):
    # check for any missing data in the df (display in descending order)
    return df.isnull().sum().sort_values(ascending=False)

def remove_col_str(df):
    # remove a portion of string in a dataframe column - col_1
    df['col_1'].replace('\n', '', regex=True, inplace=True)
    
    # remove all the characters after &# (including &#) for column - col_1
    df['col_1'].replace(' &#.*', '', regex=True, inplace=True)

def remove_col_white_space(df,col):
    # remove white space at the beginning of string 
    df[col] = df[col].str.lstrip()
 
def color_vals(val):
    color = 'blue' if val < 0 else 'black'
    return 'color: %s' % color

def color_negative_vals(df):
    """Takes a scalar and returns a string with
    the css property `'color: blue'` for negative
    strings, black otherwise."""
    return df.style.applymap(color_vals)

def highlight_max_vals(s):
    is_max = s == s.max()
    return ['background-color: red' if v else '' for v in is_max]

def highlight_min_vals(s):
    is_max = s == s.min()
    return ['background-color: lightblue' if v else '' for v in is_max]

def highlight_minmax(df):
    """Highlight the maximum and minimum in a Series/Pandas column."""
    return df.style.apply(highlight_max_vals).apply(highlight_min_vals)

def set_color(df,background_color='black',color='lawngreen',border_color='white'):
    """Set the color properties of the DataFrame; e.g., set_color(df). """
    background_color = background_color
    color = color
    border_color = border_color
    return df.style.set_properties(**{'background-color': background_color,
                           'color': color,
                           'border-color': border_color})

def make_heatmap(df,cm=sns.diverging_palette(5, 250, as_cmap=True)):
    """Create a quick heatmap, works by coloring the background
    in a gradient according to the data in each column."""
    df_heatmap = df.style.background_gradient(cmap=cm)
    return df_heatmap

def magnify_heatmap(df,cm=sns.diverging_palette(5, 250, as_cmap=True)):
    """Color negative and positive vals for each column to display
    overall trends per column and row and provide hover function 
    for inspecting individual values."""
    cmap = cm

    bigdf = df.style.background_gradient(cmap, axis=1)\
    .set_properties(**{'max-width': '80px', 'font-size': '1pt'})\
    .set_caption("Hover to magnify")\
    .set_precision(2)\
    .set_table_styles([dict(selector="th",
                 props=[("font-size", "10pt")]),
            dict(selector="td",
                 props=[('padding', "0em 0em")]),
            dict(selector="th:hover",
                 props=[("font-size", "12pt")]),
            dict(selector="tr:hover td:hover",
                 props=[('max-width', '200px'),
                        ('font-size', '12pt')])])
    return bigdf

def data_summary(X_train, y_train, X_test, y_test):
    """Summarize dataset."""
    print('Train images shape:', X_train.shape)
    print('Train labels shape:', y_train.shape)
    print('Test images shape:', X_test.shape)
    print('Test labels shape:', y_test.shape)
    print('Train labels:', y_train)
    print('Test labels:', y_test)

if __name__ == '__main__':
    main()
