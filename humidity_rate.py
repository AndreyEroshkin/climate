#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:51:00 2019

@author: aaa
"""

import pandas as pd
import re
import numpy as np
import seaborn as sns
from CoolProp.HumidAirProp import HAPropsSI
from shutil import copyfile
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

#df = pd.read_excel('/home/aaa/Documents/greenair/Запросы/18 Миас Центр релаксации/28645.01.01.2015.01.04.2019.1.0.0.ru.utf8.00000000.xls', skiprows = 6)
df = pd.read_excel('./Барнаул.xls', skiprows = 6)

df.columns

d = []
for index, row in df.iterrows():
        try:
                W = HAPropsSI('W','T',row['T']+273.15,'P',101325,'R',row['U']/100)
        except:
                W = np.nan
        d.append(W)
        
df['d'] = d

df['d'].hist()
sns.distplot(df['d'])
df.loc[:,'парит']=0
df.loc[(df['U']>=60) & (df['T']>=26),'парит']=1


sns.lmplot(y='U',x='T', hue= 'парит', data=df, fit_reg=False)


df.loc[df['d']>0.0136,['Местное время в Москве (ВДНХ)','T','U','d']]