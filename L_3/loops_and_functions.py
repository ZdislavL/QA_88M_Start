for number in range (1,11):
    if number % 2 == 0:
        continue
    print("Only odd numbers:", number)

for number in range (1,21):
    if number % 3 == 0:
        print("divided by 3:", number)

def add(a,b):
    return a + b

print(add(1,2))

res = add(10,20)
print(res)
print("Sum is -->", res)

def is_even(a):
    return a % 2 == 0

print(is_even(2))
print(is_even(3))

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([7,0,3,15])
print("Low:", low, "High:", high)

def sum_list(numbers):
    sum = 0
    for sum in numbers:
        sum += sum
    return sum

print(sum_list([1,2,3,4,5]))

def avg(numbers):
    return sum_list(numbers) / len(numbers)

print(avg([10,20,30]))

my_list = ["dog", "cat", "mouse", "fox", "rabbit"]

def count_words_longer_than_three_chars(words):
    counter = 0
    for word in words:
        if len(word) > 3:
            counter += 1
    return counter

print("Count is -->", count_words_longer_than_three_chars(my_list))

#(a, e, i, o, u)

my_list1 = ["Paris", "Berlin", "Madrid", "Rome", "Kyiv","Dnipro","Odesa"]
def count_vowels(words):
    vowels = "aeiouAEIOU"
    counter = 0
    for word in words:
        for letter in word:
            if letter in vowels:
                counter += 1
    return counter

print("Vowel count is -->", count_vowels("Python"))