#1
a_gen = (i ** 2 for i in range(1, 11))
for i in a_gen:
    print(i)

#2
a_even_gen = (i ** 2 for i in range(1, 11) if i % 2 == 0)
for i in a_even_gen:
    print(i)

#3
def gen_fib():
    f_1, f_2 = 1, 1
    while True:
        f_1, f_2 = f_2, f_1 + f_2
        yield f_2

for i in gen_fib():
    print(i)

print(gen_fib())

#4
import random
def random_num():
    while True:
        yield random.randint(1, 10)

gen_random_num = random_num()
for i in range(7):
    print(next(gen_random_num))

#5
def random_word(text):
    for word in text.split():
        yield word


text = "Hello world, how are you doing?"
for word in random_word(text):
    print(word)

#6
from random import randint
def get_ramdom_rgb():
    yield (randint(0, 255),
           randint(0, 255),
           randint(0, 255))


for i in get_ramdom_rgb():
    print(i)

#7
def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_num_gen(num_1):
    for num in range(2, num_1):
        if is_prime(num):
            yield num

num_1 = 20

for prime in prime_num_gen(num_1):
    print(prime)

#10
import random
import string

def password():
    while True:
        yield "".join(random.choice(symbols) for _ in range(password_length))


symbols = string.digits + string.ascii_lowercase + string.ascii_uppercase
password_length = 5

password_gen = password()
for _ in range(5):
    print(next(password_gen))









