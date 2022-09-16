#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[17]:


delays = pd.read_csv('Hartsfield_Jackson_Airport/Cleaned_Datasets/Cleaned_Delays', dtype = {'ORIGIN_AIRPORT' : str, 'DESTINATION_AIRPORT' : str})
flights = pd.read_csv('Hartsfield_Jackson_Airport/Raw_Data/flights.csv', dtype = {'ORIGIN_AIRPORT' : str, 'DESTINATION_AIRPORT' : str})


# In[ ]:





# In[139]:


dayDict = { 
        1 : 'Monday',
        2 : 'Tuesday',
        3 : 'Wendsday',
        4 : 'Thursday',
        5 : 'Friday',
        6 : 'Saturday',
        7 : 'Sunday'
    }
explode = (0, 0, 0, 0, 0, 0, 0)
delaysDays = pd.DataFrame()
delaysAir = pd.DataFrame()
temp = pd.DataFrame()

delaysDays['DELAYS'] = delays['DAY_OF_WEEK'].apply(lambda x : dayDict[x]).value_counts()
delaysDays['FLIGHTS'] = flights['DAY_OF_WEEK'].apply(lambda x : dayDict[x]).value_counts()

delaysDays.plot(kind = 'pie', subplots = True, figsize = (15,5), autopct='%1.2f%%', cmap = 'tab10', legend = False, 
                shadow = True, startangle=15, labeldistance=1.2, title = 'Dealy Delays to Daily Flights ', fontsize = 10)

delaysAir['AMOUNT'] = delays['AIRLINE'].value_counts()

delaysAir.drop(delaysAir[delaysAir['AMOUNT'] / delaysAir['AMOUNT'].sum() < (delaysAir['AMOUNT'].median() - delaysAir['AMOUNT'].quantile(0.25)) / delaysAir['AMOUNT'].sum()].index, inplace = True)
delaysAir.loc['OTHERS'] = delays['AIRLINE'].value_counts().sum() - delaysAir.sum()

delaysAir

delaysAir.plot(kind = 'pie', subplots = True, figsize = (15,6), autopct='%1.2f%%', cmap = 'tab20', legend = False, 
                shadow = True, startangle=15, pctdistance = 0.85, labeldistance=1.1)


# In[ ]:




