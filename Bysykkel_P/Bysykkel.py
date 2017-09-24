# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 16:22:41 2017

@author: Chiem PC
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style','default')
plt.rcParams['figure.figsize']=(15,5)

#pd.read_*,pd.read_csv
#Numpy array can be loaded into Pandas

#array = np.random.randn(8, 4)
#pd.DataFrame(array, columns=["A","B","C","D"])

#!ls -h1 ./*.csv #csv file of bysykkel
#!head ./trips-2017.8.1-2017.8.31.csv #bash command head to inspect first lines

#----------------Start data analysis---------
bike_stats = pd.read_csv('./trips-2017.8.1-2017.8.31.csv',sep=',')
print(type(bike_stats))
print(bike_stats) #pandas automatically used the first line as titles for the data columns
print(bike_stats.head()) #excerpt the first tiles

print(bike_stats[['Start time','End time']].head()) #select column by indexing title
print(bike_stats[['Start time','End time']].tail(4)) #tail to get the last elements, 

print(bike_stats.dtypes)
bike_stats_types= pd.read_csv('./trips-2017.8.1-2017.8.31.csv',sep=',', parse_dates=['Start time', 'End time']) #in order to filter by dates, we can use parse_dates arg
#print(bike_stats_types.head(2))

bike_stats_types[['Start time','Start station','End station']].head().plot(x='Start time', y=['Start station','End station'], kind="bar")

bike_stats_types[['Start station','End station']].plot('Start station', 'End station', kind="scatter")

bike_stats_types['Start station'].plot(kind='hist')

bike_stats['Start station'].value_counts()[:100].plot(kind='bar')
#-----------------saving-----
#bike_stats.to_csv("filename.csv")
#bike_stats.head().to_latex("data.tex")
#bike_stats.head().to_html("data.html")
#selecting rows bike_stats['Start time'][7:14]
#-------------check busiest station----------
