# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 14:31:50 2023

@author: prach
"""

""" 
Step1: Reading file and perfoming basic EDA 
Step2: merging data sets 
- Stores data set with train data set
- train data set with transactions data set 
Step3: EDA post merging

Findings as follows: 

"""

import pandas as pd
import numpy as np
import matplotlib as matplotlib



# importing train data 

Train_data = pd.read_csv("C:/Users/prach/OneDrive/Desktop/Time series sales data/train.csv")

Train_data.describe()
Train_data.columns

Train_data.id.min()
Train_data.id.max()
Train_data.id.count()

# there are 3000888 unique data points in train data set starts with 0 and ends with 3000887. 

Train_data.date.min()
Train_data.date.max()

Train_data['date'] = pd.to_datetime(Train_data['date'])
date = Train_data['date'].dt.date
num_days = len(date.unique())
num_days

#data ranges from 1st Jan 2013 to 15th Aug 2017, 1684 days of sales data

Train_data.store_nbr.min()
Train_data.store_nbr.max()
len(Train_data.store_nbr.unique())

# there are 54 unique strore IDs
# there is further stores data set which has attribute combinations for these Ids
# we will further merge stores data and train data to get these attribute values

Train_data.family.unique()
len(Train_data.family.unique())

# there are 33 unique families - Family is product family or category, example - Home care, Sea foof, liquor, wine, beer









