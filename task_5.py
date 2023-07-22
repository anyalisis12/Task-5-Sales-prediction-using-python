# -*- coding: utf-8 -*-
"""Task 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jcq72-VqlI6In64Sfj1BMoaWjNUvr8r5
"""

pip install --upgrade pip'

import numpy as np
import pandas as pd, datetime
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from time import time
import os
from math import sqrt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import itertools
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf,pacf
from statsmodels.tsa.arima_model import  ARIMA
from sklearn import model_selection
from sklearn.metrics import mean_squared_error, r2_score
from pandas import DataFrame
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

store = pd.read_csv('/content/store.csv')
train = pd.read_csv('/content/train.csv', index_col='Date', parse_dates=True)
test = pd.read_csv('/content/test.csv')
train.shape, test.shape, store.shape

train.head()

test.head()

store.head()

train.shape

train.head()

# Checking the data when the store is closed
train_store_closed = train[(train.Open == 0)]
train_store_closed.head()

# Check when the store was closed
train_store_closed.hist('DayOfWeek')

train_store_closed['SchoolHoliday'].value_counts().plot(kind='bar')

# Check whether there school was closed for holyday
train_store_closed['StateHoliday'].value_counts().plot(kind='bar')

# Check the null values
# In here there is no null value
train.isnull().sum()

# Number of days with closed stores
train[(train.Open == 0)].shape[0]

train[(train.Open == 1) & (train.Sales == 0)].shape[0]

store.head()

store.isnull().sum()

store['CompetitionDistance'].fillna(store['CompetitionDistance'].median(), inplace=True)

store.isnull().sum().sum()

test.head()

test.isnull().sum()

test.fillna(1, inplace=True)

test.isnull().sum().sum()

train_store_joined = pd.merge(train, store, on='Store', how='inner')
train_store_joined.head()

train_store_joined[(train_store_joined.Open == 0) | (train_store_joined.Sales==0)].shape

train_store_joined_open = train_store_joined[~((train_store_joined.Open ==0) | (train_store_joined.Sales==0))]
train_store_joined_open

plt.figure(figsize=(20, 10))
sns.heatmap(train_store_joined.corr(), annot=True)