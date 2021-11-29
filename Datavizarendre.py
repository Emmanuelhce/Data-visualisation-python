
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
df1=df[['Annee','NombreNJ','NombredeNF','NombredeNM','NombredeNA','NombredeNMai','NombredeNJ', 'NombredeNJUI','NombredeNAOUT','NombredeNS','NombredeNO','NombredeNN','NombredeND']].dropna()
df2=df[['NombreNJ','NombredeNF','NombredeNM','NombredeNA','NombredeNMai','NombredeNJ', 'NombredeNJUI','NombredeNAOUT','NombredeNS','NombredeNO','NombredeNN','NombredeND']].dropna()
df3=df[['Moi','Moyenne']].dropna()

fig, ax = plt.subplots()
ax.legend()
plt.plot(df1['Annee'],df2['NombredeNJ'])
plt.plot(df1['Annee'],df2['NombredeNF'])
plt.plot(df1['Annee'],df2['NombredeNM'])
plt.plot(df1['Annee'],df2['NombredeNA'])
plt.plot(df1['Annee'],df2['NombredeNMai'])
plt.plot(df1['Annee'],df2['NombredeNJ'])
plt.plot(df1['Annee'],df2['NombredeNJUI'])
plt.plot(df1['Annee'],df2['NombredeNAOUT'])
plt.plot(df1['Annee'],df2['NombredeNS'])
plt.plot(df1['Annee'],df2['NombredeNO'])
plt.plot(df1['Annee'],df2['NombredeNN'])
plt.plot(df1['Annee'],df2['NombredeND'])
plt.title("Evolution of birth")
plt.plot(figsize=(20,10))
plt.savefig("Evolutionofbirth.png", dpi=300)

plt.legend(('Jenuary','February ','March','April','May','June', 'July','August','September','October','November','December'),bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size': 9})
plt.show()
height=df3["Moyenne"]
width=0.07
plt.ylim(63200,65000) 
plt.xticks(rotation=27)
plt.bar(df3["Moi"] , height,width,color='y')
plt.title("Mean of birth for each months")

plt.savefig("Meanofbirths.png", dpi=300)

 
  