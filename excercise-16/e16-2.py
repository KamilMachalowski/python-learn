import csv

with open("excercise-16/files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter City name: ")

for row in data:
    if row[0] == city:
        print(row[1])