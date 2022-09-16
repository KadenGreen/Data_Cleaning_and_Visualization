#!/usr/bin/env python
# coding: utf-8

# In[219]:


import pandas as pd
import numpy as np


# In[220]:


airports = pd.read_csv('Hartsfeild_Jackson_Airport/Raw_Data/airports.csv')
fleetAnalysis = pd.read_csv('Hartsfeild_Jackson_Airport/Raw_Data/AAfleetBaseAnalysis.csv')


# In[221]:


#Changing all needed toal data to per flight and removing old columns
fleetAnalysis['GATE_COST/FLIGHT'], fleetAnalysis['FEE_COST/FLIGHT'], fleetAnalysis['TOTAL_COST/FLIGHT'] = fleetAnalysis.loc[:, 'TOTAL_GATE_COST'] / fleetAnalysis.loc[:, 'TOTAL_FLIGHTS'], fleetAnalysis.loc[:, 'TOTAL_FEES'] / fleetAnalysis.loc[:, 'TOTAL_FLIGHTS'], fleetAnalysis.loc[:, 'TOTAL_COST'] / fleetAnalysis.loc[:, 'TOTAL_FLIGHTS']  
fleetAnalysis.drop(columns = ['TOTAL_GATE_COST', 'TOTAL_FEES', 'TOTAL_COST', 'TOTAL_FUEL_COST', 'TOTAL_MAX_PASSANGERS', 'MILES_TRAVELED'])


# In[222]:


#Removing datapoints with 0 that adversely affected the means
fleetAnalysis[fleetAnalysis['TOTAL_FLIGHTS'] < 10] = None
fleetAnalysis = fleetAnalysis.dropna()


# In[223]:


fleetAnalysis = fleetAnalysis.loc[:, ['PASSENGER_CAPACITY', 'BASE_COST/FLIGHT', 'FUEL_COST/MILE', 'TOTAL_FLIGHTS', 'COST/PASSANGER', 'GATE_COST/FLIGHT', 'FEE_COST/FLIGHT', 'TOTAL_COST/FLIGHT']]
fleetAnalysis = fleetAnalysis.sort_values(by = ['PASSENGER_CAPACITY', 'TOTAL_COST/FLIGHT'], ascending = False)


# In[224]:


#Grouping the mean of all the rows into their respective model (determined by the plane capacity)
models = pd.concat([fleetAnalysis[fleetAnalysis['PASSENGER_CAPACITY'] == 524].groupby("PASSENGER_CAPACITY").mean(), fleetAnalysis[fleetAnalysis['PASSENGER_CAPACITY'] == 368].groupby("PASSENGER_CAPACITY").mean(), fleetAnalysis[fleetAnalysis['PASSENGER_CAPACITY'] == 200].groupby("PASSENGER_CAPACITY").mean(), fleetAnalysis[fleetAnalysis['PASSENGER_CAPACITY'] == 85].groupby("PASSENGER_CAPACITY").mean(), fleetAnalysis[fleetAnalysis['PASSENGER_CAPACITY'] == 21].groupby("PASSENGER_CAPACITY").mean(), fleetAnalysis[fleetAnalysis['PASSENGER_CAPACITY'] == 5].groupby("PASSENGER_CAPACITY").mean()])


# In[225]:


#Sets passenger capacity as the index, not able to acces with models if aboove, but creates blank column when removed
fleetAnalysis.set_index('PASSENGER_CAPACITY', drop = True, inplace = True)


# In[226]:


fleetAnalysis.to_csv('Hartsfeild_Jackson_Airport/Cleaned_Datasets/Clean_AAfleetBaseAnalysis_Airports.csv')
models.to_csv('Hartsfeild_Jackson_Airport/Cleaned_Datasets/Plane_Model.csv')


# In[ ]:




