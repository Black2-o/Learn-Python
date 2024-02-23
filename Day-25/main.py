# with open("226 weather-data.csv", mode="r") as data:
#     x = data.readlines(1000)

# print(x)

# import csv
# with open("226 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for row in data:
#         rows = row
#         # print(rows)
#         temp = rows[1]
#         if temp == "temp":
#             pass
#         else:
#             temprature.append(int(temp))

# # print(data)
# print(temprature)




import pandas

data = pandas.read_csv("226 weather-data.csv")
print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# avrage = sum(temp_list) / len(temp_list)
# print(avrage)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.day == "Monday"])

# max_temp_day = data[data.temp == data.temp.max()]
# print(max_temp_day)

# mondey = data[data.day == "Monday"]
# # print(mondey.condition)
# mondey_temp_in_F = mondey.temp * (9/5) + 32
# print(mondey_temp_in_F)




## Create A DAta Frame From Scartch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores":[76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


# 2018 Central Park Squirrel Census
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_count = 0 
# red_count = 0 
# black_count = 0 
# color_list = data["Primary Fur Color"].to_list()
# for color in color_list:
#     if color == "Gray":
#         grey_count += 1
#     elif color == "Cinnamon":
#         red_count += 1
#     elif color == "Black":
#         black_count += 1

# data_all = {
#     "Color": ["Grey", "Red", "Black"],
#     "Count": [grey_count, red_count, black_count]
# }

# dataX = pandas.DataFrame(data_all)
# print(dataX)
# dataX.to_csv("2018_central_park.csv")


# 2018 Central Park Squirrel Census Other Way
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_count = len(data[data["Primary Fur Color"] == "Black"])

# data_all = {
#     "Color": ["Grey", "Red", "Black"],
#     "Count": [grey_count, red_count, black_count]
# }

# dataX = pandas.DataFrame(data_all)
# dataX.to_csv("2018_central_parks.csv")