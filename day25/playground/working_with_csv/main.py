# import csv


# with open("weather_data.csv") as data:
#     data_list = data.readlines()

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])

# temperatures.remove("temp")
# for index, temp in enumerate(temperatures):
#     temperatures[index] = int(temp)


# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(round(average))

# print(data["temp"].mean())

# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data.day[data.temp == data.temp. max()])

# celsius = data.temp[data.day == "Monday"]
# fahrenheit = (celsius * (9 / 5)) + 32
# print(fahrenheit)

# create dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
