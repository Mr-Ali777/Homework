#1
num_list = []
num = 1
while num <= 10:
    num_list.append(num)
    num += 1
print(num_list)

#2
number = int(input("From keybord:"))
num_list = []
num = 1
while num < number:
    num_list.append(num)
    num += 1
print(num_list)

#2 (FOR METHOD)
number = int(input("From keybord:"))
for n in range(1,number):
    print(n)

#3
num_list = list(range(1, 20))
even_list = []
num = 1
while num < len(num_list):
    even_list.append(num_list[num])
    num += 2
print(even_list)

#3 (FOR METHOD)
num_list = list(range(1, 20))
for even in range(1, 20):
    if even % 2 == 0:
        print(even)

#4
number = int(input("From keybord:"))
num_list = []
num = 2
while num < number:
    num_list.append(num)
    num += 2
print(num_list)

#5
num = 1
num_1 = 1
while num_1 <= 10:
    num = num * 1
    print(num, '*', num_1, '=', num * num_1)
    num_1 += 1

#6
num = int(input("From keybord: "))
for i in range(1, num):
    for m in range(2, num):
     print(f"{i} * {m} = {i * m}")


#7
number = int(input("From keybord:"))
num_list = []
num = 1
while num < number:
    num_list.append(num)
    num += 1
print(num_list[::-1])

#8
words = input("From keybord:")
alphabet = ("A, E, I, O, U, Y,B, C, D, F, G, H, J, "
            "K, L, M, N, P, Q, R, S, T, V, W, X, Z")
letter_list = []
for letter in words:
    if letter in alphabet.lower():
        letter_list.append(letter)
print(letter_list)

#9
words = input("From keybord:")
letter_list = []
for letter in words:
    letter_list.append(letter)
print(letter_list[::-1])

#10
words = input("From keybord:")
for letter in words:
    if letter == 'а':
        continue
    print(letter)


                                               #(HOME WORK WITH *)
#1
words = input("From keybord:")
vowels = "ауоыиэяюёе"
counter = 0
for letter in words:
    if letter.lower() in vowels:
        counter += 1
print(words, counter)

#2
words = input("From keybord:")
counter = 0
for word in words.split():
    if 'a' in words.lower():
        counter += 1
print(counter)

#3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
array = input(" From keybord: ")
result = ""
for letter in array:
    if letter.lower() in alphabet:
     result += f"{alphabet.index(letter.lower()) + 1}"
print(result)

































