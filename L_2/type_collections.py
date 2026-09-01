from enum import unique
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mix = ["text", 56, 34.7, True, True]
empty = []

print(type(empty))
print("length of numbers:", len(numbers))
print("length of fruits:", len(fruits))

print(fruits[1])
print(fruits[::-1])
print(fruits[-1])

fruits[1] = 'orange'
print(fruits)

fruits.append('grape')
print(fruits)

fruits.insert(1, 'mango')
print(fruits)

fruits.remove("mango")
print(fruits)

last = fruits.pop()
print(last)
print(fruits)

numbers2 = [99,1,2,34,4,5,78,7,0,9,10]
print(sorted(numbers2))
print(sorted(numbers2, reverse=True))
print(min(numbers2), max(numbers2), sum(numbers2))
print("Is 34 in numbers2 -->", 34 in numbers2)

numbers2.sort()
print(numbers2)

for fruit in fruits:
    print("i like", fruit)

#tuple
coordinates1 = (10, 20)
single = (34,)
print(type(single))
print(type(coordinates1))
tuple1 = 1,2,3
print(type(tuple1))

print(coordinates1[0])
print(coordinates1[1])

x,y = coordinates1
print(f"x={x}, y={y}")

#dictionary
person = {
    "name": "Zdislav",
    "age": 32,
    "city" : "Warsaw"
}

print(person)
print("Length of my dict:", len(person))

print(person["name"])
print(person["age"])
# print(person["email"])
print(person.get("email","No email found"))

person["email"] = "sdfghj@dfgh.com"
print(person)

person["age"] = 33
print(person)

del person["email"]
print(person)

print("name" in person)
print("phone" in person)

dict_any = {
    1: "paz",
    "two": 2,
    (0,1): "rtfyu"
}

dict_any[(True,False)] = True
print(dict_any)
dict_any[(False,True)] = False
print(dict_any)

print((True,False) == (1,0))

prices = {
    "apple":21,
    "banana":4,
    "orange":3
}
for product in prices:
    print("Product:", product)

for product, price in prices.items():
    print(f"Product: {product} costs {price}$")

print(list(prices.keys()))
print(list(prices.values()))
print(sum(prices.values()))

#set
colors = {"red", "green", "blue"}
print(colors)
colors.discard("red")
print(colors)
colors.remove("green")
print(colors)
colors.add("yellow")
print(colors)
print(len(colors))

numbers_set = {1,2,2,3,4,4,5,6,6,6,7,8,9,10}

print(numbers_set)
print(len(numbers_set))
print(type(numbers_set))

empty_dict = {}
print(type(empty_dict))

empty_set = set()
print(type(empty_set))

colors.add("yellow")
print(colors)

names = ["Ivan","Olena","Taras","Taras","Roman","Oksana","Ivan"]
print(names)

unique_names = set(names)
print(unique_names)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

set1.update(set2)
print(set1)



