#1(task from lesson)
class Bank:
    def __init__(self, deposit=None):
        self.deposit = deposit
        self.is_open = True

    def open_deposit(self):
        if self.deposit is not None:
            return "Deposit already open."
        self.deposit = 0
        return "Deposit has been open"

    def close_deposit(self):
        if self.deposit is None:
            return "Deposit already close"
        self.deposit = None
        return "Deposit has been close"

    def add_money(self, amount):
        if self.deposit is None:
            return "Deposit closed"
        if self.deposit < amount:
            return "Money not enough"
        self.deposit -= amount

    def cash_in(self,amount):
        if self.deposit is not None:
            return "Deposit closed"
        self.deposit += amount

#2(task from lesson)
import sys


class Cafe:
    def __init__(self):
        self.menu = []

    def add_dish(self, dish):
        if dish not in self.menu:
            self.menu.append(dish)
            print(f"Dish '{dish}' was added to the menu.")
        else:
            print(f"Dish '{dish}' already in menu.")

    def remove_dish(self, dish):
        if dish in self.menu:
            self.menu.remove(dish)
            print(f"Dish '{dish}' was removed from the menu.")
        else:
            print(f"Dish '{dish}' not in menu.")

    def order(self, *dishes):
        ordered_dishes = [dish for dish in dishes if dish in self.menu]
        if ordered_dishes:
            print("You order this dish")
            for dish in ordered_dishes:
                print(f"- {dish}")
        else:
            print("Not incorrect order. Dish not in menu")


def launcher():
    cafe = Cafe()

    while True:
        print("1. Add dish:")
        print("2. Remove dish:")
        print("3. Make order:")
        print("4. Check menu:")
        print("4. Exit")

        choice = input("Make your choice ->")

        if choice == "1":
            dish = input("Dish name: ")
            cafe.add_dish(dish)

        elif choice == "2":
            dish = input("Dish name to remove from menu: ")
            cafe.remove_dish(dish)

        elif choice == "3":
            dishes = input("Make order : ")
            cafe.order(*dishes)

        elif choice == "4":
            print("Our menu ->")
            if cafe.menu:
                for dish in cafe.menu:
                    print(f' - {dish}')

        elif choice == "5":
            print("Exit")
            sys.exit()


launcher()

#3(task from lesson)
from datetime import datetime


class User:
    def __init__(self, name, surname, age, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.profession = profession

    def get_full_name(self):
        return f"Full name: {self.name.capitalize()} {self.surname.capitalize()}"

    def new_full_name(self, value):
        self.name, self.surname = value.split()

    def del_full_name(self):
        self.name, self.surname = None, None

    full_name = property(fget=get_full_name, fset=new_full_name, fdel=del_full_name)

    def email(self):
        return f"{self.name}.{self.surname}@mail.ru"

    def birt_year(self):
        return datetime.now().year - self.age

    def doctor(self):
        return User("Ivan", "Ivanov", 31, "doctor")

    def policeman(self):
        return User("Joe", "Luca", 31, "policeman")


u = User("Ivan", "Drago", 32, "driver")
u.full_name = "vladimir putin"
print(u.full_name)



#4(task from lesson)

from random import randint, choice


class House:
    def __init__(self, price, square):
        self.price = price
        self.square = square

    def __str__(self):
        return (f'{self.square} - '
                f'{self.price}$')

    def __repr__(self):
        return (f'{self.square} - '
                f'{self.price}$')


class Costumer:
    def __init__(self,name, account):
        self.name = name
        self.account = account

    def __str__(self):
        return (f'{self.name} - '
                f'{self.account}$')

    def __repr__(self):
        return (f'{self.name} - '
                f'{self.account}$')


def gen_house_list(count):
    house_list = []
    for _ in range(count):
        house = House(price=randint(20_000, 200_000), square=randint(20, 200))
        house_list.append(house)
    return house_list


def gen_costumer_list():
    costumer = Costumer("Ivan", account=randint(20_000, 150_000))
    return costumer

def get_recs(houses: list[House], costumer=Costumer):
    rec_houses = list(filter(lambda h: h.price <= costumer.account, houses))
    rec_houses.sort(key=lambda h: h.square, reverse=True)
    return rec_houses

def launcher():
    houses = gen_house_list(20)
    costumer = gen_costumer_list()
    print(costumer)
    recs = get_recs(houses=houses, costumer=costumer)
    return recs


print(launcher())
