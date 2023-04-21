# analyze the data
# determine the number of squirrels that are grey/red/black
import pandas
gray, red, black = 0, 0, 0

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# for color in data["Primary Fur Color"]:
#     if color == "Gray":
#         grey += 1
#     if color == "Cinnamon":
#         red += 1
#     if color == "Black":
#         black += 1

gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
    "color": ["gray", "red", "black"],
    "number": [gray, red, black]
}

new_csv = pandas.DataFrame(color_dict)
new_csv.to_csv("squirrel_count.csv")
