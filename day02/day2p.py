# DATATYPES, NUMBERS, OPERATORS, TYPECONVERSIONS AND F-STRINGS
#Datatypes
name = "tmk"
age = 20
height = 6.2
single =True
#subscripting
print("Hello"[0])
print("Hello"[-1])

money = 2_00_000 #large numbers can be represented by this
print(money)
#Type casting / Type conversions

print(type(age)) #output <class 'int'>
print(str(age)) #output <class 'str'>
print(type(height)) #output <class 'float'>
print(int(height)) #output <class 'int'>

# Operators
print(2+3)
print(3-2)
print(4*2)
print(3/2) #always gives float (python implicit conversion)
print(4**2)
print(3//2) #gives the interger output
#Number manipulation
number = 54.34245245242555
print(round(number))
print(round(number,2))
#operations and f-strings
number = 10
number+=1
print(f"number incremented by 1 : {number}")



