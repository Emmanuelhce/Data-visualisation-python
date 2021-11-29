# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 15:31:06 2021

@author: Manu
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:22:05 2021

@author: Manu
"""
import pandas as pd
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

from pandas_datareader import data as pdr
df= pd.read_excel(r'C:\Users\emman\Desktop\datavizassignement\NombredeN.xlsx')
df.head()
col_names = df.columns.tolist()
print(col_names)
df1=df[['Période','Nombre de naissance']].dropna()
plt.xticks(rotation=70)
plt.plot(df1['Période'],df1['Nombre de naissance'])
plt.title("Births in France from 1946")
plt.gca().set_xticks(plt.gca().get_xticks()[::100]) #As they where too many ticks, it would reduce the number by 100
plt.axhline(y=81000, color='r')
plt.axhline(y=49000, color='r')
plt.show()
plt.savefig("MeanofbirthsinFrance.png", dpi=300)


