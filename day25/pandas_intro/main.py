# Comma Separated Values, a common way to export data in tables, like Excel or Google Sheets
# Open the csv file. use .readlines() to create a list named 'data' that contains all the values from the csv file.
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     # data is a csv.reader object
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data["temp"][0])

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# Entire table is stored in data, columns are known as 'series' in pandas

# average = sum(temp_list) / len(temp_list)
# print(data["temp"].mean())

# print(data["temp"].max())

# Get data in columns
# data["condition"] or data.condition

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# celsius = monday.temp
# fahrenheit = celsius * 9/5 + 32
# print(fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
