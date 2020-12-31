import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
final_dict = {
        "Colors":[],
        "Count": []
}
for color in data['Primary Fur Color'].unique():
    #Exists a Nan data in DataFrame
    if type(color) is str:
        final_dict["Colors"].append(color)
        final_dict["Count"].append(data[data['Primary Fur Color'] == color]['Primary Fur Color'].count())


data = pandas.DataFrame(final_dict)
data.to_csv("Squirrel_Census.csv")
