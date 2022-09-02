## import packages
import pandas as pd
import datetime as dt
import uuid 
import numpy as np

## 1. load in data
df = pd.read_csv('data/School_Learning_Modalities.csv')
df

## 2. get number of rows and columns
df.shape

## 3. list column names
list(df)

## 4. clean column names
# remove all special characters and whitespace ' ' from column names  # regex
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')

# replace all whitespace in column names with an underscore
df.columns = df.columns.str.replace(' ', '_')
list(df)

## 5. clean strings that might exist within columns
# get column types list, want to see if strings are really strings, number are numbers, dates are dates, and boolean are booleans
df.dtypes

