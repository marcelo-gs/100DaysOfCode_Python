import pandas
#import csv

#with open('weather_data.csv') as weather_file:
#    data  = csv.reader(weather_file)
#    temperature = []
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))


data = pandas.read_csv('weather_data.csv')
print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

print(data['temp'].mean()) #media
print(data['temp'].max()) #max value

#get columns
print(data['condition'])
print(data.condition) #pandas create an atributte for each column

#get data in row
print(data[data.day == "Monday"])

### getting the row that has the max temp 
print(data[data.temp == data.temp.max()])

###
monday = data[data.day == "Monday"]
print(monday.condition)

### Create a dataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"], 
    "scores": [76,56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
