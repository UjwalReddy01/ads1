#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 22:25:21 2023

@author: ujwalreddy
"""

#Importing Pandas package to read the file 
import pandas as pd
#Importing matplotlib python package for data plotting and visualization
import matplotlib.pyplot as plt

#defining function for lineplot and plotting the graph
def lineplot(col_a,col_b,col_c,label_a,label_b,label_c):
    plt.figure()
    plt.plot(matches[col_a],linewidth=2,label=label_a)
    plt.plot(matches[col_b],linewidth=2,label=label_b)
    plt.plot(matches[col_c],linewidth=2,label=label_c)
    plt.xlabel('Year',fontsize=15)
    plt.ylabel('Temperatures',fontsize=15)
    plt.title('Year & Different Temperatures b/w 1979 to 2020 ',fontsize=15)
    plt.legend(loc='upper center')
    plt.show()

#defining function for pie chart and plotting the graph 
def pie_chart(snow_depth,title,Year):
    plt.figure()
    #countries =['1980','1985','2000','2005']
    plt.pie(matches[snow_depth],labels=Year,autopct=('%0.1f%%'))
    plt.title(title)
    plt.legend(loc =2 ,bbox_to_anchor=(1,1.2))
    plt.show()
    
#defining function for barchart and plotting the graph
def barchart(col_a,col_b,label_a,label_b,title,x_label,y_label):
    plt.figure(figsize=(10,10))
    plt.bar(matches[col_a],matches[col_b],width=0.4,label=label_a)
    plt.xlabel(x_label,fontsize=20)
    plt.ylabel(y_label,fontsize=20)
    plt.title(title,fontsize=20)
    plt.legend(prop={'size':16})
    plt.show()    
    
#defining columns and reading the file
columns = ['max_temp','mean_temp','min_temp','snow_depth']
matches = pd.read_csv('london_weather.csv',nrows=4,usecols=columns)   

#calling the function for lineplot
lineplot('max_temp','mean_temp','min_temp','max_temp','mean_temp','min_temp') 

#calling the function for pie_chart
pie_chart('snow_depth','Snow depth of four years',['1980','1985','2000','2005'])

#calling the function for barchart
barchart('max_temp','mean_temp','max_temp','mean_temp','temperatures probability','temperatures','Probability')

    