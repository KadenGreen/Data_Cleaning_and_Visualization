#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import pandas as pd


# In[8]:


flights = pd.read_csv('Hartsfield_Jackson_Airport/Raw_Data/flights.csv', dtype = {'ORIGIN_AIRPORT' : str, 'DESTINATION_AIRPORT' : str})

#Changes time format to be rounded to the nearest 15 minuites
flights['SCHEDULED_DEPARTURE'] = flights['SCHEDULED_DEPARTURE'].apply(lambda x: int(x / 100) * 100 + (round(x % 100 /15) * 15) if ((round(x % 100 /15) * 15) != 60) else (int(x / 100) * 100 + (round(x % 100 /15) * 15) + 40))



#Creating two dataframes that individually hold the delays the airport it liable for (airportDelay) and delays that the 
#airlines are liable for (flightsDelay) to be later exported and visualized
airportDelay = flights[['MONTH', 'DAY', 'DAY_OF_WEEK', 'AIRLINE', 'DESTINATION_AIRPORT', 'SCHEDULED_DEPARTURE','DIVERTED', 'CANCELLED', 'CANCELLATION_REASON']]
delays = flights[['MONTH', 'DAY', 'DAY_OF_WEEK', 'AIRLINE','ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'SCHEDULED_DEPARTURE', 'DEPARTURE_DELAY', 'TAXI_OUT',  'TAXI_IN', 'WHEELS_OFF', 'AIR_TIME', 'DISTANCE', 'AIR_SYSTEM_DELAY', 'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY']].dropna()


#Creating two seperate dataframes for airportDelay to see patters for which flights were delayed (airportDelayD) and patterns
#for flights that were canceled (airportDelayC)
airportDelayD = airportDelay[airportDelay['DIVERTED'] != 0].drop(columns = ['CANCELLED', 'CANCELLATION_REASON']).copy()
airportDelayC = airportDelay[airportDelay['CANCELLED'] != 0].drop(columns = ['DIVERTED']).copy()

airportDelayD.set_index('MONTH', inplace = True)
airportDelayC.set_index('MONTH', inplace = True)
delays.set_index('MONTH', inplace = True)

flights


# In[3]:


airportDelayD.to_csv('Hartsfield_Jackson_Airport/Cleaned_Datasets/Flights_Airport_Delay_Diverted.csv')
airportDelayD


# In[4]:


airportDelayC.to_csv('Hartsfield_Jackson_Airport/Cleaned_Datasets/Clean_Airport_Delay_Cancelled.csv')
airportDelayC


# In[5]:


delays.to_csv('Hartsfield_Jackson_Airport/Cleaned_Datasets/Cleaned_Delays')
delays


# In[ ]:




