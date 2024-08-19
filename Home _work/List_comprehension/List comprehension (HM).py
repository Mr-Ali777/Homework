#1
a = int(input("Num 1: "))
b = int(input("Num 2: "))
print([n ** 2 for n in range(a, b + 1)])

#2
a = int(input("Num 1: "))
b = int(input("Num 2: "))
num_list = []
for num in range(a, b + 1):
    num_list.append(int(num))
print(num_list)
print([even for even in num_list if even % 2 == 0])

#3
array = input("From keybord :")
print([ord(letter) for letter in array])

#4
print([num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0])

#5
print([[x for x in range(1, 5)], [y for y in range(5, 9)], [z for z in range(9, 13)]])

                                                #(OTHER)
#2
number = int(input("From keybord:"))
str_number = str(number)
print([max(num) for num in max(str_number)])

                                               #5 (IN ONE STR)
num_list = [22, 4, 1, 32, 15, 20, 5, 12, 47, 11]
print([sqr ** 2 for sqr in num_list])
print([float(num) % 11 for num in num_list])
print([even for even in num_list if even % 2 == 0])
print([num for num in num_list if num % 2 != 0])
print([num for num in num_list if num % 3 != 0])

