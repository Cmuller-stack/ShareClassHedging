#!/usr/bin/env python
# coding: utf-8

# # Shares Class Hedging

# In[98]:


import numpy as np
import array as arr
import pandas as pd
import matplotlib.pyplot as plt


# ## Open file

# In[220]:


file = pd.read_excel("/..../..../../NAV.xlsx", header=0, parse_dates= True)
df = pd.DataFrame(file)
df.head()


# ## Show NAV evolution Class EUR and USD Funds

# In[225]:


plt.plot(df['Months'], df['NAV Classe EUR'], 'b',label= 'NAV Classe EUR')
plt.plot(df['Months'], df['NAV Fonds USD'], 'g', label= 'NAV Fonds USD')
plt.title('NAV')
plt.legend()
plt.ylabel('NAV')
plt.xlabel('Période')
plt.xticks(rotation='vertical')
# plt.savefig("/.../...../.../return.png", dpi=200) 
plt.show


# ## Calculation monthly return and display plot
# 

# In[418]:


returns = (df[columns].iloc[1:]/df[columns].iloc[:-1].values-1)
returns.head()


# In[409]:


plt.plot(df['Months'].iloc[1:], returns['NAV Classe EUR'], 'b',label= 'NAV Classe EUR')
plt.plot(df['Months'].iloc[1:], returns['NAV Fonds USD'], 'g', label= 'NAV Fonds USD')
plt.title('Monthly Return')
plt.legend()
plt.ylabel('return (%)')
plt.xlabel('Période')
plt.xticks(rotation='vertical')
#plt.savefig("/.../.../.../return.png", dpi=200) 
plt.show


# ## Calculation total return cumulative and display plot

# In[426]:


cumul_return =((returns+1).cumprod()-1)*100
cumul_return.head()


# In[425]:


plt.plot(df['Months'].iloc[1:], cumul_return['NAV Classe EUR'], 'b',label= 'NAV Classe EUR')
plt.plot(df['Months'].iloc[1:], cumul_return['NAV Fonds USD'], 'g', label= 'NAV Fonds USD')
plt.title('Cumulaive Return')
plt.legend()
plt.ylabel('return (%)')
plt.xlabel('Période')
plt.xticks(rotation='vertical')
#plt.savefig("/.../.../.../return.png", dpi=200) 
plt.show


# ## Plot spot EUR/USD

# In[446]:


file_hedging = pd.read_excel("/.../.../.../PtsForwards.xlsx", header=0, parse_dates= True)
df_hedging = pd.DataFrame(file_hedging)
df_hedging.head()


# In[444]:


plt.plot(df_hedging['Months'].iloc[0:], df_hedging['Spot EURUSD'], 'b',label= 'Spot EURUSD')
plt.title('Spot EUR/USD')
plt.legend()
plt.ylabel('EUR/USD')
plt.xlabel('Période')
plt.xticks(rotation='vertical')
#plt.savefig("/.../.../.../return.png", dpi=200) 
plt.show


# ## Calculation of cost of heding

# In[480]:


# calculation
date= df_hedging['Months']
pts_forwards_bp = df_hedging['1m Mid FWD points (pp)']/10000
forwards_eurusd = df_hedging['Spot EURUSD']+ pts_forwards_bp
monthly_implicit_cost = (df_hedging['Spot EURUSD']/forwards_eurusd-1)
monthly_implicit_cost_pct =monthly_implicit_cost*100
monthly_implicit_cost_cumul =((monthly_implicit_cost+1).cumprod()-1)
monthly_implicit_cost_cumul_pct= monthly_implicit_cost_cumul*100

# resume of results
recap_tab = {
    "Date": date,
    "Spot EURUSD": df_hedging['Spot EURUSD'],
    "Pts Forwards bp":pts_forwards_bp,
    "Forwards EURUSD":forwards_eurusd,
    "Monthly implicit hedging cost (%)":monthly_implicit_cost_pct,
    "Cumulative Cost of Hedging (%)":monthly_implicit_cost_cumul_pct
}

recap_tab_df = pd.DataFrame(recap_tab)
recap_tab_df.head()


# In[495]:


plt.plot(recap_tab_df['Date'].iloc[0:], recap_tab_df['Monthly implicit hedging cost (%)'].iloc[0:], 'g',label= 'Monthly implicit hedging cost (%)')
plt.title('Monthly Implicit cost of Hedging (%)')
plt.legend()
plt.ylabel('Monthly Implicit cost of Hedging (%)')
plt.xlabel('Période')
plt.xticks(rotation='vertical')
#plt.savefig("/.../.../.../Project Share class Hedging/MICoH", dpi=200) 
plt.show


# In[ ]:




