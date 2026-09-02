try:
    res = 10/1
    print("Res is",res)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Hi")

input_str = "slksf"

try:
    number = int(input_str)
    print(number)
except ValueError:
    print("Cannot convert to int")

print("Hii!")

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    finally:
        print("Division completed")

print(divide(10,2))
print(divide(10,0))


try:
    numbers = [1, 2, 3]
    print(numbers [3])
except IndexError as e:
    print(e)
    print(type(e).__name__)


def divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        print(e)

divide(1, "python")

data = {"name": "John", "age": 30}

try:
    print(data["city"])
except KeyError as e:
    print("Key Error:", e)
except Exception:
    print("Unexpected error!")
finally:
    print("Completed")

try:
    number = int("456")
except ValueError:
    print("Only integer")
else:
    print("Success, it is a number:", number)


try:
    print("Try part")
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Always finished")

def type_age(age):
    try:
        age = int(age)
    except (TypeError,ValueError):
        print("Age must be an integer")
    else:
        print("Age is:", age)

type_age("23")
type_age("Hi")
