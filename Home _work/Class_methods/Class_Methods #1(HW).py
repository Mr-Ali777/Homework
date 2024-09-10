#1
import random

class Book:
    def __init__(self, title, author, page_num, publication_year):
        self.title = title
        self.author = author
        self.page_num = page_num
        self.publication_year = publication_year

#2
class Car:
    def __init__(self, manufacturing, model, year, color):
        self.manufacturing = manufacturing
        self.model = model
        self.year = year
        self.color = color


    def engine():
        return "Engine turn on"


print(Car.engine())



#3
class Fridge:
    def __init__(self, manufacturing, volume, model):
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

#4
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

#5
class Home:
    def __init__(self,floors, rooms, sqr):
        self.floors = floors
        self.rooms = sqr
        self.sqr = sqr

    def home_price():
        return "Count home price"


print(Home.home_price())

#6
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

#(task from class)
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

#(home work 1)
from random import randint, choice


CARS = {"Germany": ["BMW", "VW", "Audi", "Opel"],
        "USA": ["Dodge","GMC", "Chevrolet", "Ford"],
        "Russia": ["VAZ", "LADA", "Aurus"]}


class Car:
    __TOTAL_OBJECT = 0

    def __init__(self, manufacturing, country, millage):
        self.manufacturing = manufacturing
        self.country = country
        self.millage = millage
        Car.__TOTAL_OBJECT += 1

    def __eq__(self, other):
        if not isinstance(other, Car):
            return AttributeError(f"<{other}> object must be Car instance, not {type(other)}")
        if self.country.lower() != other.country.lower():
            return False
        return True

    def zero_millage(self, new_millage=0):
        self.millage = new_millage

    @staticmethod
    def get_instance_count():
        return Car.__TOTAL_OBJECT

    def __repr__(self):
        return f"{self.manufacturing, self.country, self.millage}"


def gen_class_cars(count: int):
    res = []
    for _ in range(count):
        country = choice(list(CARS.keys()))
        car = Car(
                manufacturing=choice(CARS[country]),
                country=country,
                millage=randint(10_000, 70_000))
        res.append(car)
        return res


def cars_sort(cars_list: list[CARS], parameter : str):
    match parameter:
        case "manufacturing":
            cars_list.sort(key=lambda x: x.manufacturing)
        case "country":
            cars_list.sort(key=lambda x: x.country)
        case "millage":
            cars_list.sort(key=lambda x: x.millage)
        case _:
            return ValueError("Parameter incorrect. Choices manufacturing , country, millage")
    return cars_list


cars = gen_class_cars(2)
print(cars_sort(cars_list=cars, parameter="millage"))

#(home work 2)
class Snow:
    def __init__(self, count):
        self.count = count

    def make_snow(self, in_row):
        full_rows = self.count // in_row
        last_row = self.count - (full_rows * in_row)
        for _ in range(full_rows):
            print("*" * in_row)
        print("*" * last_row)

    def __add__(self, other):
        self.count += other

    def __sub__(self, other):
        self.count -= other

    def __mul__(self, other):
        self.count *= other

    def __truediv__(self, other):
        self.count /= other


s = Snow(14)
s.make_snow(3)





