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

## 6. assess white space or special characters by removing it with a script
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')

## 7. convert the column types to the correct types by first seeing if date is on weekday or weekend
df['Week'] = pd.to_datetime(df['Week'])
df['Week'] = pd['Week'].dt.dayofweek

## 8. look for duplicate rows and remove duplicate rows
df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)

## 9. assess missingness (count of missing values per column)
df.isnull().sum()

## 10. create a new column called modality_inperson that contains a binary value of true or false
df['modality_inperson'] = np.where(df["Learning_Modality"] == 'In Person', True, False)
df.dtypes

## 11. save the clean data into a cvs file
df.to_csv('data/Clean_School_Learning_Modalities.csv')