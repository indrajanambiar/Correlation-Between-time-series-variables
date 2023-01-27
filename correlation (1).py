#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt


# In[19]:


df=pd.read_csv("DailyDelhiClimateTest.csv")
df


# In[20]:


df.shape


# In[21]:


df.info()


# In[22]:


df.describe()


# In[ ]:





# In[23]:


df.isnull().sum()


# In[29]:


df['wind_speed%']=df['wind_speed'].pct_change()
df['humidity%']=df['humidity'].pct_change()


# In[30]:


correlation = df['humidity'].corr(df['wind_speed'])
print(correlation)


# In[31]:


#The Pearson correlation coefficient measures the linear relationship between two variables. 
#It ranges from -1 to 1, where -1 indicates a perfect negative correlation, 
#0 indicates no correlation, and 1 indicates a perfect positive correlation.


# In[ ]:





# In[32]:


window_size = 30 # specify the size of the rolling window
roll_coef = df['humidity'].rolling(window=window_size).corr(df['wind_speed'])
print(roll_coef)


# In[ ]:




