# with open("weather_data.csv") as file:
#     data = file.readlines()
import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data)

temp_list = data["temp"].to_list()
print(temp_list)

avg = data["temp"].mean()
print(avg)
max = data["temp"].max()
print(max)

print(data.condition)

# Get data in rows
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.temp[0] * 9 / 5 + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")

# squirrel stuff below
print("--------squirrels are in my pants S.I.M.P--------------------")
# create fur color and count columns of each type of squirrel
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240405.csv")
squirrels_count = len(squirrel_data["Unique Squirrel ID"].to_list())

print(f"total squirrels in NYC Central Park: {squirrels_count}")

cinnamon_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(black_squirrel_count)

squirrels_dict = {
    "Fur": ["cinnamon", "gray", "black"],
    "Count": [cinnamon_squirrel_count, gray_squirrel_count, black_squirrel_count]
}
squirrels = pandas.DataFrame(squirrels_dict)
squirrels.to_csv("squirrels_count.csv")
