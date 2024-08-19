#1
number = int(input("Введеное число: "))
if number <0 and number != 0:
   print("Отрицательный")
elif number > 0:
   print("Положительный")
else:
   print("Является нулем")

#2
a = float(input("Длинна стороны a: "))
b = float(input("Длинна стороны b: "))
c = float(input("Длинна стороны c: "))
if a == b and b == c and c == a:
   print("Равносторонний")
elif a != b and b != c and c != a:
   print("Разносторонний")
elif a == b or b == c or a == c:
   print("Равнобедренный")

#3
word = input("Введенное слово: ")
print(tuple(word))
first_letter = word[0]
if first_letter in word.lower():
   print("Начинается с малой буквы нижнего регистра")
else:
   print("Начинается с буквы верхнего регистра")

#4
symbol = input("Введенный символ: ")
vowels = ("а, у, о, ы, и, э, я, ю, ё, е")
consonants = ("б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ")
if symbol in vowels:
   print("Гласный")
elif symbol in consonants:
   print("Согласный")

#5
numbers = input("Введенные числа: ")
list_numbers = list(numbers.split(","))
a = list_numbers[0]
b = list_numbers[1]
c = list_numbers[2]
if a < b and a < c:
   print(a)
elif b < a and b < c:
   print(b)
elif c < a and c < b:
   print(c)
elif a == b == c:
   print("Равны")

#6
str_1 = input("Первая строка: ").lower()
str_2 = input("Вторая строка: ").lower()
if len(tuple(str_1)) > len(tuple(str_2)):
   print("Первая строка содержит больше символов")
elif len(tuple(str_2)) > len(tuple(str_1)):
   print("Вторая строка содержит больше символов")
else:
   print("Количество символов в строках равны")







