import csv
with open("./day25/weather_data.csv") as data_file:
  data = csv.reader(data_file)
  temperatures = []

  for row in data:
    if row[1] != "temp":
      temperatures.append(int(row[1]))

  print(temperatures)

  #Even in this also there is include more faff and if we have so much data it gonna get more difficult so, because of this we take help of pandas library