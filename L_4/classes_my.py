class Fruit: 
    def __init__(self, name, weight): 
        self.name = name
        self.weight = weight

fruit1 = Fruit(name="Apple", weight=10)
fruit2 = Fruit(name="Banana", weight=20)

print(fruit1.name, fruit1.weight)
print(fruit2.name, fruit2.weight)
fruit1.weight = 40

print(fruit1.name, fruit1.weight)
print(fruit2.name, fruit2.weight)

class Fruit:
    def __init__(self, name, day_ripe):
        self.name = name
        self.day_ripe = day_ripe
        
    def describe(self):
        print(f"Fruit name: {self.name}")

    def wait_a_day(self):
        self.day_ripe -= 1
        print(f"The {self.name} will be ripe in {self.day_ripe} days")
        
    def is_ripe(self):
        return self.day_ripe <= 0

apple = Fruit("Apple", 2)
apple.describe()
apple.wait_a_day()
print(apple.is_ripe())
apple.wait_a_day()
print(apple.is_ripe())

class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2
    
c1 = Circle(2)
c2 = Circle(5)

print("Area is:", c1.area())
print("Area is:", c2.area())

print("Pi is", Circle.pi)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account of {self.owner} with balance {self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrawn", amount, "Balance", self.balance)

    def get_balance(self):
        return self.balance


account = BankAccount("John", 1000)
print(account)
account.deposit(500)
print(account)
account.withdraw(100)
print(account)
account.withdraw(2000)
#print(account.__balance)
print(account.get_balance())

class Animal: 
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

    def make_sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} barks")

    def swim(self):
        print(f"{self.name} is swimming")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows")

    def play(self):
        print(f"{self.name} is playing with the ball")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.eat()
dog.make_sound()
cat.eat()
cat.make_sound()
cat.play()
dog.swim()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Marks: {self.marks}"

student = Student("Ivan", 20, 90)
print(student)



# perimetr (a+b)*2 area a*b

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: Width {self.width}, Height {self.height}"
    
    def perimetr(self):
        return (self.width + self.height) * 2
    
    def area(self):
        return self.width * self.height

rectangle = Rectangle(2, 4)
print(rectangle)
print("Perimetr is -->", rectangle.perimetr())
print("Area is -->", rectangle.area())

#celsius
class Thermometer:
    def __init__(self):
        self.__temperature = -273

    def set_temperature(self, t):
        if t > -273:
            self.__temperature = t
        else:
            print("Thermometer can't lower -273")

    def get_temperature(self):
        return self.__temperature


term = Thermometer()
print(term.get_temperature())
term.set_temperature(25)
print(term.get_temperature())