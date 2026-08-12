import pandas

data = pandas.read_csv("./day25/weather_data.csv")
# print(data["temp"])

#The primary datastructues in pandas are dataframes and series
#Dataframes are kind of the whole table like this
print(type(data))
print(data)

#Series are kind of single column like a list like this
print(type(data["temp"]))
print(data["temp"])
#You can also do some crary things using pandas. Just read and understand documentation. Mainly api section having all the ways you can use pandas.

#The best thing is you can do conversion like from series to list (All you have to do is to read documentation.)
temperatures = data["temp"].to_list()
print(temperatures)

#Here we are findings the mean temperature of week.
average_temp = sum(temperatures) / len(temperatures)
print(f"Average of temperatures is {average_temp}")
#Instead of doing all this. we can use some series computations methods that comes from pandas.
print(data["temp"].mean())

#Finding max among the temperatures using one of the data series method.
print(f"The maximum temparature that was recored in the week is {data['temp'].max()}")

#You can get series wheather using dict method or using object method.
#dict method - You treat the column name as key and get its values
print(data["day"])
#object method - pandas takes all names convert them into attrributes.
print(data.day)
#THE BOTH GIVE THE SAME THING DONT WORRY ABOUT IT.

#Here comes the little bit harder part and that is how to get row of data in dataframe
print(data[data.day == "Monday"])

#find the row having highest temperature in the week
print(data[data.temp == data.temp.max()])

#Can go little further and also find indiviuals from the rows
monday = data[data.day == "Monday"]
print(monday.condition)

#Showing the monday's temperature in fahrenheit
mon_temp = monday["temp"]

fah = (mon_temp*(9/5)) +32
print(fah)

#How to create a dataframe from scratch
student_details = {
  "student_name" : ["tmk","rishi","roshan"],
  "scores" : [99,98,97],
}
data = pandas.DataFrame(student_details)
print(data)
data.to_csv("./day25/new_csv.csv")