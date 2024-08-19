#1
import string
import random


def password():
    symbols = string.digits + string.ascii_lowercase + string.ascii_uppercase
    password_size = random.randint(8, 15)
    return "".join(random.choice(symbols) for pas in range(password_size))


print(password())

#1 (решение 2)
from random import randint, choice


def num() -> str:
    pasw = ''
    for _ in range(randint(3, 5)):
        digit = chr(randint(48, 57))
        letter_lwr = chr(randint(97, 122))
        letter_upper = chr(randint(65, 90))
        pasw += digit + letter_lwr + letter_lwr
    return pasw


print(num())


#2
from random import randint, choice


NAMES = ["Walter", "Gustavo", "Jessie", "Bob", "Tom", "Vicktor", "Vitya"]
num_temp = "+375(29){}{}{}-{}{}-{}"
contact_list = []


def get_contact(count: int):
       c_num = num_temp.format(*[randint(1, 9) for _ in range(7)])
       contact ={choice(NAMES): c_num}
       contact_list.append(contact)

#3
def game(player_1: str, player_2: str):
    dict_1 = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if dict_1[player_1] == player_2:
        return player_1
    if dict_1[player_2] == player_1:
        return player_2
    else:
        return "DRAW"


print(game(player_1="rock", player_2= "paper"))


#4
from random import randint, choice

def phone_number(array: list) -> str:
    return "({}{}{}){}{}{}-{}{}-{}{}".format(*array)


print(phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


