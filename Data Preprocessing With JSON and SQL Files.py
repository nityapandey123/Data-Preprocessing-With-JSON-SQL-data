#!/usr/bin/env python
# coding: utf-8

# # Working With JSON

# In[9]:


import pandas as pd


# In[2]:


pd.read_json('train.json')


# # Json Data with url

# In[3]:


pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')


# #    Working with SQL

# In[4]:


get_ipython().system('pip install mysql.connector')


# In[5]:


import mysql.connector


# In[6]:


conn = mysql.connector.connect(host='localhost',user='root',password='',database='world')


# In[7]:


df = pd.read_sql_query("SELECT * FROM countrylanguage",conn)


# In[8]:


df


# In[ ]:




