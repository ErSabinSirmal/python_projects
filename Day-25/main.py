# with open("weather_data.csv") as data:
#     weather_report = data.readlines()
# print("List of name is: ")
# print(weather_report)
# for row in weather_report:
#     print(row)
#
# #
# # # We can import csv to print the list in the readable format
#
# import csv
#
# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

#     # for item in temperature[1:]:
#     #     tempr = int(item)
#     #     print(tempr)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data["condition"]))

#  # dataframe conversion
# # print((data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
# # #
# temp_list = data["temp"].to_list()
# print(len(temp_list))
# print(temp_list)
# # #
# # # average_tempr = sum(temp_list) / len(temp_list)
# # # print(average_tempr)
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # # Get Data in columns
# print(data["condition"])
# print(data.condition)
#
# #get data in Row
#
# print(data[data.day == "Monday"])
# maximum = data.temp.max()
# print(data[data.temp == maximum])
#
# tuesday = data[data.day == "Tuesday"]
# print(tuesday.condition)
#
# tempreture = data[data.day == "Monday"]
# print(tempreture)
# print(tempreture.temp)
# temp_fahrenheit = (tempreture.temp * 9/5) + 32
# print(temp_fahrenheit)
#
# # create a dataframe from scratch
#
# data_dict  = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# my_data = pandas.DataFrame(data_dict)
# print(my_data)
#
# #converting the dataframe to the csv file
# my_data.to_csv("new_data1.csv")



# squirrel census data analysis...

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

my_squirrels = pd.DataFrame(data_dict)
print(my_squirrels)
my_squirrels.to_csv("squirrel_count.csv")
print(my_squirrels["Count"].to_list())



