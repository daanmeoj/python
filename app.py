
from pathlib import Path
from collections import namedtuple
from abc import ABC, abstractmethod
from timeit import timeit
from sys import getsizeof
from array import array
from collections import deque
import math
str = "hello world"

print(str[0:3])

print("Hi there ")

print("*"*10)

print("hello world")

2+3
x = 1
y = 2
unit_prince = 3

students_count = 1000
rating = 4.99
is_published = False
print(students_count)

#############################STRINGS#######################################################
course_name = "Python Programming"
message = """
    Hi John,

    this is mosh from...

"""
print(len(course_name))

print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])

course = "Python \"Programming"

course = "Python \nProgramming"

print(course)

first = "mosh"
last = "Hamedani"
full = f"{first} {last}"
print(full)

print(first.upper())
print(first.lower())
print(full.title())


input2 = "       python programming"

print(input2.strip())
print(input2.lstrip())
print(input2.rstrip())

print(input2.find("py"))
print(input2.find("hola"))
print(input2.replace("p", "y"))
print("pro" in input2)
print("swift" not in input2)


#############################NUMBERS#######################################################
x = 1
x = 1.1
x = 1+2j

print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10 % 3)
print(10**3)

x = 10
x += 3
print(x)

#import math

print(round(2.9))
print(abs(-2.9))


print(math.ceil(1.1))

# x = input("x:")
# y = int(x)+1
# print(type(x))
# float(x)
# bool(x)
# str(x)
# print(f"x: {x}, y: {y}")

# FALSY
# ""
# 0
# None
print(bool(0))
print(bool(1))
print(bool(""))
print(bool(None))


###################CONTROL FLOW#################################################
print("bag" > "apple")

print("bag" == "BAG")

print(ord("b"))
print(ord("B"))


temperature = 8
if temperature > 30:
    print("Its warm")
    print("Drink water")
elif temperature > 20:
    print("its nice")
else:
    print("its cold")
print("Done")


print("bag" > "apple")


age = 12
# if age >= 18:
#     message = "Elegible"
# else:
#     message = "Not Eligible"


message = "Elegible" if age >= 18 else "Not Eligible"

print(message)


# and
# or
# not
high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Elegible")
else:
    print("Not Elegible")


age = 22

if 18 <= age < 65:
    print("Elegible")

for number in range(3):
    print("attempt", number+1, (number+1)*".")

for number in range(1, 4):
    print("attempt", number, (number)*".")


for number in range(1, 10, 2):
    print("attempt", number, (number)*".")


successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted three times and failed")


# if we never break


# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")


# for x in "hola mundo":
#     print(x)

# for x in [1, 2, 3, 4, 5]:
#     print(x)


# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print("we have 4 even number")


##########################functions###############################################################
def greet(first_name, last_name):
    print(f"hi there {first_name} {last_name}")
    print("welcome aboard")


greet("David", "Mercado")
greet("David", "Mercado")


def get_greet(first_name, last_name):
    return f"hi there {first_name} {last_name}"


greet1 = get_greet("David", "Mercado")
file = open("content.txt", "w")
file.write(greet1)

print(greet("David", "Mercado"))


def increment(number, by=2):
    return number+by

# optional parameters should be placed to the right of required parameters


print(increment(2, by=1))

print(increment(2))


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print("start")
print(multiply(2, 3, 10))
print("end")

# f9 add breakpoint
# f5 run until breakpoint
# f10 step over
# f11 setp into
# Shift+f5 stop debbuger
# Shift+f11 step out


def save_user(**user):
    print(user)
    print(user["id"])


save_user(id=1, name="john", age=22)

# python automatically package it in a dictionary

message = "a"


def greet2(name):
    global message
    message = "b"


greet2("Mosh")
print(message)


def FizzBuzz(variable):
    if (variable % 3 == 0) and (variable % 5 == 0):
        return "FizzBuzz"
    if variable % 3 == 0:
        return "Fizz"
    if variable % 5 == 0:
        return "Buzz"
    return variable

    FizzBuzz(15)

# move line up-----> press alt and up arrow

# copy line -----> select it and press shift+alt+arrow

# data structures#########################3


letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 3]]
zeroes = [0]*5
print(zeroes)
combined = zeroes+letters
print(combined)
numbers = list(range(20))
letras = list("hello world")
print(numbers)
print(letras)
letters[0] = "A"
print(letters[0])
print(letters[-1])
print(letters)
print(letters[0:3])
print(letters[:3])
print(letters[0:])
print(letters[:])
print(letters[::2])
numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])
numbers2 = [1, 2, 3]
# first = numbers2[0]
# second = numbers2[1]
# third = numbers2[2]
first, second, third = numbers2
print(third)

numbers3 = [1, 2, 2, 3, 4, 4, "a", "-", 4]
first, second, *other = numbers3
print(first)
print(other)
first, *other, second = numbers3
print(first)
print(second)

for index, number in enumerate(numbers3):
    print(index, number)

# add

numbers3.append("a")
print(numbers3)
numbers3.insert(0, "c")
print(numbers3)

# remove
numbers3.pop()
print(numbers3)
numbers3.pop(1)
print(numbers3)
numbers3.remove(4)
print(numbers3)
del numbers3[0]
print(numbers3)
del numbers3[0:3]
print(numbers3)
print(numbers3.index("a"))
if "o" in numbers3:
    print(numbers3.index("o"))
print(numbers3.count(4))

array1 = [54, 6, 1, 67, 100, 2]
array1.sort()
print(array)
array1.sort(reverse=True)
print(array1)
print(sorted(array1, reverse=True))

items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 5),
    ("Product4", 2)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


items.sort(key=lambda item: item[1])
print(items)

prices = []
for item in items:
    prices.append(item[1])

print(prices)


x = list(map(lambda item: item[1], items))
x = [item[1] for item in items]  # using list comprehension
# for item in x:
#     print(item)

print(x)

filtered = []

x = list(filter(lambda item: item[1] >= 10, items))
x = [item for item in items if item[1] >= 10]
print(x)


list1 = [1, 2, 3]
list2 = [10, 20, 30]

# [(1, 10), (2, 20), (3, 30)]
print(list(zip("abc", list1, list2)))


browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
browsing_session.pop()
print(browsing_session)
print("redirect ", browsing_session[-1])
browsing_session.pop()
browsing_session.pop()

if not browsing_session:
    print("disable")


queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

if not queue:
    print("empty")

point = (1, 2)
print(type(point))
point += (2, 3)
point *= 3
print(point)
point2 = [1, 2]
point2 = tuple(point2)
print(point2)
greet4 = "hello world"
print(tuple(greet4))
print(tuple(greet4[0:3]))

# a tuple is inmutable

x = 10
y = 11

z = x

x = y
y = z

x, y = y, x


print(x)
print(y)

aNumbers = array("i", [1, 2, 3])
aNumbers[0] = 6
print(aNumbers[0])


# set is a collection with no duplicates
numbers = [1, 1, 2, 2, 2, 4, 4]

uniques = set(numbers)
second = {2, 4}
second.add(7)
print(uniques)
print(second)
print(uniques | second)  # union

print(uniques & second)  # intersection


print(uniques - second)  # difference

print(second-uniques)  # difference

print(second ^ uniques)  # symetric difference

if 1 in uniques:
    print("yes")

dict1 = {"x": 1, "y": 2}
dict1 = dict(x=1, y=2)
dict1["x"] = 10
dict1["z"] = 30
print(dict1)
print(dict1["x"])
if "a" in dict1:
    print(dict1["a"])
print(dict1.get("a"))
print(dict1.get("a", 0))
del dict1["x"]
print(dict1)
for key in dict1:
    print(key, dict1[key])

for key, value in dict1.items():
    print(key, value)

values = []

for x in range(5):
    values.append(x*2)

print(values)

values = [x*2 for x in range(5)]
print(values)

values = {x*2 for x in range(5)}
print(values)


values = {x: x*2 for x in range(5)}
print(values)


values = (x*2 for x in range(5))
print(values)


values = (x*2 for x in range(10000))
print("gen: ", getsizeof(values))
# print(values)
# for x in values:
#     print(x)
values = [x*2 for x in range(10000)]
print("list: ", getsizeof(values))


numbers = [1, 2, 3]
print(*numbers)


values = list(range(5))
values = [*range(5), *"hello"]
print(values)

first = [1, 3]
second = [7, 8]
total = [*first, *second]
print(total)

dict2 = dict(x=1)
dict3 = dict(x=10, y=2)
combined = {**dict2, **dict3, "z": 1}
print(combined)


sentence = "This is a common interview question"
print("Start")
dict4 = {}
for letter in sentence:
    if letter in dict4:
        dict4[letter] = dict4[letter]+1
    else:
        dict4[letter] = 1
print(dict4)

max = -1000
for key, value in dict4.items():
    if value > max:
        max = value
print(max)


A0 = dict(zip(("a", "b", "c", "d", "e"), (1, 2, 3, 4, 5, 6)))
print(A0)
A1 = reversed(range(10))
print(A1)
A2 = [i for i in A1 if i in A0]
print(A2)
A3 = list(map(lambda x: x*3, A2))
print(A3)

# numbers = [1, 2]
# print(numbers[3])
# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("you didnt enter a valid age")
#     print(ex)
#     print(type(ex))
# else:
#     print("no exceptions were thrown.")
# print("execution continue")


# try:
#     age = int(input("Age: "))
#     xfactor = 10/age
# except ValueError:
#     print("you didnt enter a valid age")
# except ZeroDivisionError:
#     print("you didnt enter a valid age")
# else:
#     print("no exceptions were thrown.")
# try:
#     # automatically release external objects
#     with open("app.py") as file:
#         print("file opened")  # content manager protocol
#     age = int(input("Age: "))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print("you didnt enter a valid age")
# else:
#     print("no exceptions were thrown.")

code1 = """

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/0


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
    # print(error)
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/0


xfactor=calculate_xfactor(-1)
if xfactor==None:
    pass
"""

print("first code", timeit(code1, number=10000))
print("second code", timeit(code2, number=10000))


# classes

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x},{self.y})")

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


Point.default_color = "yellow"
point = Point(10, 20)
print(type(point))
print(isinstance(point, Point))
print(point.x)
point.draw()
point.z = 10
print(point.z)
another = Point(4, 3)
another.draw()
print(point.default_color)
print(Point.default_color)
point2 = Point.zero()
point2.draw()
print(point2)

other = Point(1, 2)
print(point == other)
print(point > other)
print(point < other)
combined = point+other
print(combined)


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def iter(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("java")
cloud.add("java")
cloud["python"] = 10
print(cloud["python"])
print(len(cloud))
# print(cloud.__tags)
print(cloud.iter)
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.__dict__)
print(cloud._TagCloud__tags)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value

    # price = property(get_price, set_price)


product = Product(10)
# product.price = -1
print(product.price)


# inheritance

class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):

    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
m.eat()
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))
o = object()  # creating an empty object
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))


class Bird(Animal):
    def fly(self):
        print("fly")


class chicken(Bird):
    pass


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()

# from abc import ABC,abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


# class MemoryStream(Stream):
#     pass

class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory")


stream = MemoryStream()
stream.open()
stream.read()


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")


# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")


# def draw(controls):
#     for control in controls:
#         control.draw()

# Duck typing
class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
# print(isinstance(ddl, UIControl))
# ddl.draw()
textBox = TextBox()
draw([ddl, textBox])

# it is a better practice to have an abstract class


# class Text(str):

#     def duplicate(self):
#         return self+self


# text = Text("Python")
# print(text.lower)

class TrackeableList(list):
    def append(self, object):
        print("append called")
        super().append(object)


list1 = TrackeableList()
list1.append("1")

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
# by default python compare the address in memory of each object
print(id(p1))
print(id(p2))


# from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)


# python standard libraries


# from pathlib import Path
# Path("usr/local/bin")
path = Path("ecommerce/__init__.py")
# Path()/"ecommerce"/"__init__.py"
# Path.home
print(path.exists())
print(path.is_file())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_suffix(".txt")
# path = path.with_name("file.txt")
print(path)
print(path.absolute)


for number in numbers:
    print(number)


samples = [[1, 1, 1], [1, 1, 0], [1, 0, 0]]
print(samples)


def largestArea(samples):
    T = [[0 for x in range(len(samples[0]))] for y in range(len(samples))]

    max = 0
    for i in range(len(samples)):
        for j in range(len(samples[0])):
            T[i][j] = samples[i][j]
            if i > 0 and j > 0 and samples[i][j] == 1:
                T[i][j] = min(T[i][j-1], T[i-1][j], T[i-1][j-1])+1
            if max < T[i][j]:
                max = T[i][j]
    return max


print(largestArea(samples))


# ingresosPorMes = []
# deseoContinuar = input("desea continuar (SI/NO): ")
# userId = 0
# while(deseoContinuar.lower() == "si"):
#     for i in range(5):
#         print("mes numero")
#         print(i)
#         ingresoMes = input("ingrese ingresos mes ")
#         nombreMes = input("ingrese nombre del mes")
#         dependientesMes = input("ingrese numero de dependientes")
#         item = [ingresoMes, nombreMes, dependientesMes, userId]
#         ingresosPorMes.append(item)
#     userId = userId+1
#     deseoContinuar = input("desea continuar (SI/NO): ")
# print(ingresosPorMes)
