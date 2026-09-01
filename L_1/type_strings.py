age = 18 # int
price = 19.99 # float
name = "Sveta" # str
is_name = True # bool

fruits = ["apple", "orange"] # list
coordinates = (1, 2, 3) # tuple
student = {"name": "Sveta", "age": 18} # dict
unique_numbers = {1, 2, 3, 3, 3, 4, 4} # set

print(unique_numbers)
print(type(age))
print(type(price))
print(type(name))

s1 = "Viktor"
s2 = "I want to say \"Hi\" "
print (s1 + s2)
s3 = "First string \nSecond string \nThird string"
print(s3)
first_name = "Petya"
last_name = "Sidorov"
full_name = first_name + " " + last_name
print(full_name)
long_string = "Hello World "*5
print(long_string)

word = "Privet"
print(word[0])
print(word[3])
print(word[1:4])
print(word[1:])
print(word[1:len(word)])
print(word[:2])
print(word[::-1])
print(word[-1])

text3 = "   i enjoy walking   "
text4 = "hello python"

print(text3)
print(text3.lower())
print(text3.upper())
print(text3.title())
print(text4.capitalize())

print(text3.strip())
print(text3.lstrip())
print(text3.rstrip())

print(text3.strip().replace("walking", "hiking"))

text5 = "i like walking"
parts = text5.split(" ")
print(parts)
print(" ,".join(parts))
print(text5.find("walking"))

print("abracadabra".count("a"))
print("34526".isdigit())
print("sdflkj".isalpha())
print("Hello Python 123".isalnum())

# 31.08.2026 "Year: 2026, Month: 08, Day: 31"
date_str= "31.08.2026"
date_str.split(".")
print("Year: 2026, Month: 08, Day: 31".format(date_str.split(".")[2], date_str.split(".")[1], date_str.split(".")[0]))
