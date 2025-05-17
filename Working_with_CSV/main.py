import csv
import pandas as pd

# with open('weather-data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pd.read_csv('weather-data.csv')

temp_list = data['temp'].to_list()
# print(data['temp'].max())
# print(data[data.temp == data.temp.max()])


