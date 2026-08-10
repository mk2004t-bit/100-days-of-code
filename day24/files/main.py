#First exercise is without using "with" keyword.

file = open("day24/my_file1.txt")
content = file.read()
print(content)
file.close()

#Using with so you dont have to close the file everytime you open it.
#READ - By default the mode is read.so we dont need to write it in the open.
with open("day24/my_file2.txt") as file:
  contents = file.read()
  print(contents)
#WRITE - With write can add text in the file. But he existing text deleted
with open("day24/my_file2.txt",mode="w") as file:
  file.write("This is a just a empty file 2")

#APPEND - It just add the text.Doesn't delete the existing text.
with open("day24/my_file2.txt",mode="a") as file:
  file.write("\nThis line is added using APPEND.")

#If the mode is "w" and doesn't contain that writing file. Then it creates that file for you.
with open("day24/my_file3.txt",mode="w") as file:
  file.write("This line is created by file itself using \"w\" mode.")
