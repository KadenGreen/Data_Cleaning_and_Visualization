#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd


# In[32]:


data = pd.read_csv('Hartsfeild_Jackson_Airport/Raw_Data/ATL_daily_profit.csv')

#Unifying naming conventions
data.rename(columns = {"Unnamed: 0":"DOW", "INBOUND FLIGHTS":"INBOUND_FLIGHTS", "OUTBOUND FLIGHTS":"OUTBOUND_FLIGHTS"}, inplace = True)

#naming convention confusing
data.rename(columns = {"PROFIT": "NET_REVENUE"}, inplace = True)
 
#Serve same function, creating less rows
data['DAILY_DELAY_COST'] = data.loc[:, (['AIR_SYSTEM_DELAY_COST', 'SECURITY_DELAY_COST'])].sum(axis = 1)
data.drop(['AIR_SYSTEM_DELAY_COST','SECURITY_DELAY_COST'], axis = 1, inplace = True)

#Creating the gross profit for the day
data['GROSS_REVENUE'] = data.loc[:, (['GATE_REVENUE', 'AIRLINE_DELAY_REVENUE'])].sum(axis = 1)
data.drop(['GATE_REVENUE', 'AIRLINE_DELAY_REVENUE'], axis = 1, inplace = True)

#dropping all the NaN values from October
data.dropna(inplace = True)
data.reset_index(drop = True, inplace = True)


# In[33]:


#Creating a dictionary to create the Day Of Week (DOW) column, 0 = Thursday because 1/1/15 is on a Thursday
weekday = {
    0 : "Thursday",
    1 : "Friday",
    2 : "Saturday",
    3 : "Sunday",
    4 : "Monday",
    5 : "Tuesday",
    6 : "Wendsday"
}

#Creates column of the days of the week
data['DOW'] = data['DOW'].apply(lambda x: weekday[x % 7]) 
#data.head(7)


# In[38]:


#creating new df for weekly and monthly cost and profit analysis
delay = data[['DOW', 'INBOUND_FLIGHTS','OUTBOUND_FLIGHTS', 'DAILY_DELAY_COST', 'NET_REVENUE','GROSS_REVENUE']]

#Sums all the daily delays to find the total length
#Creates warning, false positive detection
delay['DAILY_DELAY_LENGTH'] = data.loc[:,('AIR_SYSTEM_DELAY','SECURITY_DELAY','SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY')].sum(axis = 1)

#Reorganizing the rows for more logical ordering
delay = delay.loc[:, ['DOW', 'INBOUND_FLIGHTS', 'OUTBOUND_FLIGHTS', 'DAILY_DELAY_LENGTH', 'DAILY_DELAY_COST', 'GROSS_REVENUE', 'NET_REVENUE']]

delay.head(5)


# In[40]:


delay.to_csv('Hartsfeild_Jackson_Airport/Cleaned_Datasets/Clean_ATL_Daily_Profit.csv')

