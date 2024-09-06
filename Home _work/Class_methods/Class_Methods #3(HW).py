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
        Animal.__init__(name)
        self.color = color

    def __str__(self):
        return f'Mammal : {self.name}, color: {self.color}'

    def __repr__(self):
        return f"Mammal(name ='{self.name}', color= '{self.color}')"


class Fish(Animal):
    def __init__(self, name, weight):
        Animal.__init__(name)
        self.weight = weight

    def __str__(self):
        return f'Fish : {self.name}, weight: {self.weight}kg'

    def __repr__(self):
        return f"Fish(name ='{self.name}', weight ={self.weight})"


class Cat(Mammals):
    def __init__(self, name, color, species):
        Animal.__init__(name, color)
        self.species = species

    def __str__(self):
        return f'Cat : {self.name}, species: {self.species}, color: {self.color}'

    def __repr__(self):
        return f"Cat(name ='{self.name}', species ={self.species}, color ={self.color})"


class Sturgeon(Fish):
    def __init__(self, name, weight, lenght):
        Animal.__init__(name, weight)
        self.lenght = lenght

    def __str__(self):
        return f'Sturgeon : {self.name}, weight: {self.weight}kg, lenght: {self.lenght}cm'

    def __repr__(self):
        return f"Sturgeon(name ='{self.name}', weight ={self.weight}, lenght ={self.lenght})"


dog = Mammals("собака", "черный")
fish = Fish("Окунь", 34)
cat = Cat("Кот","серый","персидский")
sturgeon_fish = Sturgeon("Белуга",120,270)

print(dog)
print(fish)
print(cat)
print(sturgeon_fish)
