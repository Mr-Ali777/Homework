month_number = int(input("Месяц года: "))
time_of_year = {"winter": (12, 1, 2), "spring": (3, 4, 5), "summer": (6, 7, 8), "authum": (9, 10, 11)}
event_description = {"winter": "За окном падал белый снег", "spring": "Птицы пели прекрасные песни",
                    "summer": "Солнце светило ярче чем когда-либо", "authum": "Урожай был невероятным"}
month_name = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
             7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

if month_number in time_of_year["summer"]:
   print("Вы родились :", month_name[month_number], event_description["summer"])
elif month_number in time_of_year["authum"]:
   print("Вы родились :", month_name[month_number], event_description["authum"])
elif month_number in time_of_year["winter"]:
   print("Вы родились :", month_name[month_number], event_description["winter"])
elif month_number in time_of_year["spring"]:
   print("Вы родились :", month_name[month_number], event_description["spring"])
else:
   print("Ошибка")

#2
a = int(input("Число 1 :"))
b = int(input("Число 2 :"))
c = int(input("Число 3 :"))
if a + b < c:
   print("Меньше")
elif a + b > c:
   print("Больше")
elif a + b == c:
   print("Равно")

#3
num = input("Введенное число :")
tuple_num = tuple(num)
digit_1 = num[0]
digit_2 = num[1]
print(digit_1, digit_2)
if int(digit_1) == int(digit_2):
   print("Да это число:", num)
else:
   print("Нет")

#4
word = input("Введенное слово: ")
if len(word) >= 1:
   print("True")
elif len(word) <= 0:
   print("False")

#5
num = int(input("Введенное число:"))
numbers = str(num)
num_1 = numbers + numbers
num_2 = numbers + numbers + numbers
result = num + int(num_1) + int(num_2)
print(result)

#6
randome_dictionary = {"name": "Ali", "surname": "Farhat"}
randome_dictionary["age"] = 31
randome_dictionary[("hight", "weighj")] = [182, 110]
print(randome_dictionary.get("name"))
randome_dictionary.pop("surname")
print(randome_dictionary.keys())

#7
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)