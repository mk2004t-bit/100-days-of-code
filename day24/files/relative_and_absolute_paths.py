#Working with files using absolute file path.

with open("/Users/tmk/Desktop/my_file3.txt") as file:
  content = file.read()
  print(content)

#Working with files using " relative file " " path.
# /Users/tmk/Developer/python/100_days_of_code is my working directory.
with open("../../../Desktop/my_file3.txt") as file:
  content = file.read()
  print(content)
