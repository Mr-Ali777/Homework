#1
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Animal name: {self.name}'

    def __repr__(self):
        return f"Animal (name ='{self.name}')"

    def __eq__(self, other):
        return self.name == other.name


class Mammals(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def __str__(self):
        return f'Mammal : {self.name}, color: {self.color}'

    def __repr__(self):
        return f"Mammal(name ='{self.name}', color= '{self.color}')"


class Fish(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def __str__(self):
        return f'Fish : {self.name}, weight: {self.weight}kg'

    def __repr__(self):
        return f"Fish(name ='{self.name}', weight ={self.weight})"


class Cat(Mammals):
    def __init__(self, name, color, species):
        super().__init__(name, color)
        self.species = species

    def __str__(self):
        return f'Cat : {self.name}, species: {self.species}, color: {self.color}'

    def __repr__(self):
        return f"Cat(name ='{self.name}', species ={self.species}, color ={self.color})"


class Sturgeon(Fish):
    def __init__(self, name, weight, lenght):
        super().__init__(name, weight)
        self.lenght = lenght

    def __str__(self):
        return f'Sturgeon : {self.name}, weight: {self.weight}kg, lenght: {self.lenght}cm'

    def __repr__(self):
        return f"Sturgeon(name ='{self.name}', weight ={self.weight}, lenght ={self.lenght})"


dog = Mammals("Чарли", "черный")
dog_1 = Mammals("Боб", "белый")
fish = Fish("Нэммо", 34)
fish_1 = Fish("Русалка", 55)
cat = Cat("Бигги","серый","персидский")
cat_1 = Cat("Биглз", "рыжий", "британец")
sturgeon_fish = Sturgeon("Белуга",120,270)

print(dog)
print(dog_1)
print(fish)
print(fish_1)
print(cat)
print(cat_1)
print(sturgeon_fish)

#2
class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def get_name(self):
        return f"name: {self.name.capitalize()}"

    def new_name(self, value):
        self.name = value

    def dell_name(self):
        self.name = None

    human_name = property(fget=get_name, fset=new_name, fdel=dell_name)

    def get_age(self):
        return f"age: {self.age}"

    def new_age(self, value):
        self.age = value

    def dell_age(self):
        self.age = None

    human_age = property(fget=get_age, fset=new_age, fdel=dell_age)

    def get_height(self):
        return f"height: {self.height}"

    def new_height(self, value: int):
        self.height = value

    def dell_height(self):
        self.height = None

    human_height = property(fget=get_height, fset=new_height, fdel=dell_height)


h = Human("Vitya",19, 180)
h.human_name = "Petya"
h.human_age = 24
h.human_height = 170
print(h.name, h.age, h.height)

#3
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return f"radius: {self.radius}"

    def set_radius(self, value: int):
        self.radius = value

    circle_radius = property(fget=get_radius, fset=set_radius)

    def circle_square(self):
        square = math.pi * (self.radius ** 2)
        return f'Square : {round(square, 3)}'


r = Circle(10)
r.set_radius = 8
print(r.set_radius)
print(r.circle_square())

#4
class Bank:
    def __init__(self, deposit = None):
        self.deposit = deposit

    def get_deposit(self):
        return f"deposit: {self.deposit}$"

    def set_deposit(self, value: int):
        self.deposit = value
        if value < 0:
            print("Amount cant be negative!")
        else:
            self.deposit = value

    bank_deposit = property(fget=get_deposit,fset=set_deposit)

    def add_money(self, amount):
        self.deposit += amount
        print(f"Operation done, this amount -> {amount}$ successfully add on your deposit. "
              f"Remain balance on deposit {self.deposit}$")

    def withdraw_money(self, amount):
        if amount <= 0:
            return "Amount must be positive!"
        if amount > self.deposit:
            print("You dont have enough money on your deposit.")
        self.deposit -= amount
        print(f"Operation done, you withdraw -> {amount}$. Remain money on deposit -> {self.deposit}$")


bank = Bank(0)
bank.add_money(50)
bank.withdraw_money(60)
print(bank.deposit)

#5
class Phone:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    def get_model(self):
        return f"model: {self.model}"

    def new_model(self, value):
        self.model = value

    phone_model = property(fget=get_model, fset=new_model)

    def get_color(self):
        return f"color: {self.color}"

    def new_color(self, value):
        self.color = value

    phone_color = property(fget=get_color, fset=new_color)

    def get_price(self):
        return f"price: {self.price}"

    def new_price(self, value: int):
        self.price = value
        if value <= 0:
            print("Price cant be less then 0")
        else:
            self.price = value

    phone_price = property(fget=get_price, fset=new_price)

    def discount(self, discount=None):
        self.discount = discount

    def phone_price_with_discount(self):
        discount = (self.price * self.discount) / 100
        new_price = self.price - discount
        return f'Include discount {self.discount}%. New phone price is {new_price}$'

phone_1 = Phone("Samsung", "Black", 500)
phone_1.phone_price = 900
print(phone_1.phone_price)
phone_1.discount(15)
print(phone_1.phone_price_with_discount())

#6
class Great_Warrior:

    RANKS = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage',
             'Elite', 'Conqueror', 'Champion', 'Master', 'Greatest']

    def __init__(self):
        self.level = 1
        self.rank = 0
        self.expirience = 100
        self.achievements = []

    def level(self):
        level_1 = self.level
        return level_1

    def level_change(self):
        self.level = self.expirience // 100

    def check_level(self):
        return f'{self.level}'

    fighter_level = property(fget=check_level)

    def rank(self):
        return Great_Warrior.RANKS[self.rank]

    def rank_up(self):
        if self.expirience >= 1000 and self.rank < len(Great_Warrior.RANKS) - 1:
            self.rank += 1

    fighter_rank = property(fget=rank)

    def expirience_up(self, value):
        if self.expirience > 10000:
            self.expirience = 10000
        if self.expirience < 10000:
            self.expirience += value
            self.level = 100

    def expirience_check(self):
        return f'{self.expirience}'

    fighter_expirience = property(fget=expirience_check)

    def achievements(self):
        achievements_1 = self.achievements
        return achievements_1

    def training(self, training_name, training_expirience, training_level):
        if self.level >= training_level:
            self.expirience += training_expirience
            self.achievements.append(f'{training_name}')
            return training_name
        else:
            pass

    def battle(self, enemy_lvl):

        if 100 > self.level < 1:
            return "Invalid level"

        elif self.level == enemy_lvl.level:
            self.expirience_up(10)
            self.level_change()
            return "A good fight"

        elif self.level - enemy_lvl.level == 1:
            self.expirience_up(5)
            self.level_change()
            return "A good fight"

        elif self.level - enemy_lvl.level >= 2:
            self.expirience_up(0)
            return "Easy fight"

        elif enemy_lvl.level - self.level >= 1 and enemy_lvl - self.level <= 5:
            self.expirience_up(20*(enemy_lvl.level - self.level)*(enemy_lvl.level - self.level))
            return "An intense fight"
        else:
            return "You have been defeated"


b_lee = Great_Warrior()
f_lee = Great_Warrior()
b_lee.training("googling", 100, 1)
f_lee.training("smoking", 10000, 21)
print(b_lee.fighter_rank)
print(b_lee.fighter_level)
print(b_lee.fighter_expirience)
print(b_lee.achievements)























