#1
products = ["apple", "milk", "orange"]
count = [1, 3, 12]
dict_1 = {}
for i in range(len(products)):
    dict_1[products[i]] = count[i]
print(dict_1)

#1 (other type)
# def create_dict(product: list, counts: list) ->dict:
#     if not len(product) == len(counts):
#         return "Error"
#     result = dict()
#     for i in range(len(product)):
#         try:
#           result[product[i]] = counts[i]
#         except:
#
#     return result
# print(create_dict(["apple", "milk", "orange"],[1, 3, 12] ))


#1 (using zip)
def create_dict(product: list, counts: list) ->dict:
    return dict(zip(product,counts))
print(create_dict(["apple", "milk", "orange"],[1, 3, 12] ))


#2
def simple_number(number: int):
    number = int(input("Введите число :"))
    for num in range(2, (number // 2) + 1):
        if number % num == 0:
            return number, "-> Сложное число"
    return number, "-> Простое число"


print(simple_number(number=0))

#2 (oter way)

def is_prime(num):
    for i in range(2, int(num ** 0,5) +1):
        if num % i == 0:
            return False
        return True

user_value = input()

while user_value != 'exit':
    try:
      print(is_prime(int(user_value)))
    except ValueError:
        print("Not correct char")
print(user_value)

#4
def the_greater_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return the_greater_common_divisor(b, a % b)

def the_smallest_common_divisor(x, y):
     return (x /the_greater_common_divisor(x, y)) * y

x = int(input("Введите число 1 -> "))
y = int(input("Введите число 1 -> "))

print(int(the_smallest_common_divisor(x, y)))

#5

from random import randint

def get_rand(ln):
    return [randint(1, 5) for _ in range(ln)]


def counter(array: list[int]) -> int:
    print(array)
    uniq_elems = set(array)
    count = 0
    for elem in uniq_elems:
        if array.count(elem) > 1:
            count += 1
    return count

print(counter(array=get_rand(20)))