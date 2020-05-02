# https://realpython.com/working-with-large-excel-files-in-pandas/
# To read a large excel file with Pandas, and possibly make changes in it.
# Just, go crazy with Pandas, experiment with the stuff.
# 01/05/2020 (1st May 2020)

import pandas as pd

#Read the File
data = pd.read_csv("F:\Coding\Large Excel with Pandas\Accidents7904.csv", low_memory=False)
print("Total number of rows is", len(data))

#Print columns in the file
# print(data.columns)
# print(data['Day_of_Week'][:100])

#See columns
# print(list(data))

#Drop duplicates and missing values
# data = data.drop_duplicates().dropna()
# print("Total number of rows after dropping duplicates and missing values is", len(data))

#Accidents which happened on a Sunday
print("Accidents\n-------")
sunday = data[data.Day_of_Week == 1]
print("Number of Sunday accidents = ", len(sunday))

#Total accidents on each day of the week
# gru = data.groupby(['Day_of_Week']).size()
# print(gru)

#Display more than one column. Notice the double square brackets. Haven't figured out that one yet.
# print(data[['Day_of_Week', 'Number_of_Vehicles']])

#Sunday Accidents with more than 20 vehicles
Lotsa_acc = data[(data.Day_of_Week == 1) & (data.Number_of_Vehicles >= 20)]
print("Accidents on Sundays involving more than 20 vehicles - ", len(Lotsa_acc))

#Sunday accidents, >= 20 vehicles, in the rain
More_lotsa_acc = data[(data.Day_of_Week == 1) & (data.Number_of_Vehicles >= 20) & (data.Weather_Conditions ==2)]
print("Accidents on a rainy Sunday involving more than 20 vehicles - ", len(More_lotsa_acc))

#Accidents in London on a Sunday
london = data[data['Police_Force'] == 1 & (data.Day_of_Week == 1)]
print("Accidents in London on a Sunday - ", len(london))

#London Sunday accidents in the year 2000
london_2000 = london[(pd.to_datetime(london['Date']) >= pd.to_datetime('2000-01-01')) & (pd.to_datetime(london['Date']) <= pd.to_datetime('2000-12-31'))]
print("Sunday accidents in London in 2000 - ", len(london_2000))

#Save London 2000 data to an Excel
writer = pd.ExcelWriter("F:/Coding/Large Excel with Pandas/London 2000.xlsx", engine='xlsxwriter')
london_2000.to_excel(writer)
writer.save()
