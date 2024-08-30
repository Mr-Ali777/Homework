import random

class Book:
    def __init__(self, title, author, page_num, publication_year):
        self.title = title
        self.author = author
        self.page_num = page_num
        self.publication_year = publication_year


class Car:
    def __init__(self, manufacturing, model, year, color):
        self.manufacturing = manufacturing
        self.model = model
        self.year = year
        self.color = color

    def engine():
        return "Engine turn on"


print(Car.engine())


class Fridge:
    def __init__(self,manufacturing, volume, model):
        self.manufacturing = manufacturing
        self.model = model
        self.volume = volume
    def open_door():
        return "Open fridge door"

    def close_door():
        return "Close fridge door"

    def turn_on():
        return "Turn on fridge"


print(Fridge.open_door())
print(Fridge.close_door())
print(Fridge.turn_on())


class Human:
    def __init__(self,name, surname, age, phone_num):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_num = phone_num

    def stand_up():
        return "Stand up"

    def seat_down():
        return "Seat down"


print(Human.stand_up())
print(Human.seat_down())

class Home:
    def __init__(self,floors, rooms, sqr):
        self.floors = floors
        self.rooms = sqr
        self.sqr = sqr

    def home_price():
        return "Count home price"


print(Home.home_price())


class Student:
    def __init__(self, name, surname, age, points):
        self.name = name
        self.surname = surname
        self.age = age
        self.points = points

    def average_point():
        return "Count average point"

    def achievements():
        return "get information about achievements"


print(Student.average_point())
print(Student.achievements())


class Soda:
    def __init__(self, topping=None):
        self.topping = topping

    def show_my_drink(self):
        if self.topping is not None:
            return f'Soda with {self.topping}'
        return "Just soda without topping"


s = Soda(topping="water")
s_2 = Soda(topping="gaz")

print(s.show_my_drink())
print(s_2.show_my_drink())

#not finish yeat
# class Car:
#     def __init__(self, manufacturing, country, millage):
#         self.manufacturing = manufacturing
#         self.country = country
#         self.millage = millage
#
#
#     def gen_class(c):
#         brands = []
#         country = []
#         cars = []
#         for m in range(c):
#             manufacturing = random.choice(brands)
#             country = random.choice(country)
#             millage = random.randint(0,99999)
#             car = Car(manufacturing, country, millage)
#             cars.append(car)
#         return cars





