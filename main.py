import csv
import pandas

data = pandas.read_csv("data.csv")

#print(data['temp'])

data_dict = data.to_dict()

print(data_dict)
temp_list = data["temp"].to_list()
average_temp = sum(temp_list)/ len(temp_list)
print(average_temp)

print(data['temp'].max())


