import pandas

s_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
dataframe = pandas.DataFrame(s_data)
gray_color = len(dataframe[dataframe["Primary Fur Color"] == "Gray"])
black_color = len(dataframe[dataframe["Primary Fur Color"] == "Black"])
cinnamon_color = len(dataframe[dataframe["Primary Fur Color"] == "Cinnamon"])

squirrel_colors = {
    "Colors": ["Gray", "Black", "Cinnamon"],
    "Number": [gray_color, black_color, cinnamon_color]
}
new_dataframe = pandas.DataFrame(squirrel_colors)
print(new_dataframe)
new_dataframe.to_csv("squirrel_colors.csv")


# gray = 0
# black = 0
# cinnamon = 0
#
# for row in fur_color:
#
#     if row == "Gray":
#         gray += 1
#     elif row == "Cinnamon":
#         cinnamon += 1
#     elif row == "Black":
#         black += 1
# print(gray)
# print(black)
# print(cinnamon)
#
# dictorial = {
#     "Colors": ["Gray", "Cinnamon", "Black"],
#     "Number of Squirrels": [gray, cinnamon, black]
# }
# new_dataframe = pandas.DataFrame(dictorial)
# print(new_dataframe)



# s_data_dict = s_data.to_dict()
# fur_color = s_data_dict["Primary Fur Color"]
# print(fur_color)
# fur = pandas.DataFrame(fur_color)
# print(fur)



# data_dict = {
#     "Students": ["Amy", "James", "Angela"],
#     "Scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_html("./data.html")

#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg_temp = sum(temp_list) / len(temp_list)
# print(data.temp)
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
# fahrenheit = (monday.temp * 1.8) + 32
# print(fahrenheit)
#
#
#
#
# # print(data[data.temp == data.temp.max()])
#
# # print(data["temp"].max())