#1
def even_num(array: list) -> list:
    return list(filter(lambda x: x % 2 == 0, array))
print(even_num([2, 11, 26, 4, 91, 10, 48]))

#2
sum_numbers = lambda a, b: a + b
print(sum_numbers(3, 4))

#3
def len_string(lst:str) -> list:
    return list(filter(lambda x: len(x) > 3, lst))
print(len_string(["amkdkak","sds","kkdk","www"]))

#4
def sqr_num(lst:int) -> list:
    return list(map(lambda x: x ** 2, lst))
print(sqr_num([1, 2, 3, 4, 5, 6, 7]))

#5
def words(lst:str) ->list:
    return list(filter(lambda x: x.startswith('a') or x.startswith("A"), lst))
print(words(["Hello", "ali","Arizona","Pyhton"]))

#6
def nums(lst:int) -> list:
    return list(filter(lambda x: x > 10, lst))
print(nums([12, 5, 22, 1, 9, 10, 7]))

#7
def word(lst:str)-> list:
    return list(map(lambda x: x.upper(), lst))
print(word(["Hello", "ali","Arizona","Pyhton", "friend"]))

#8
def nums(lst: int) -> list:
    return list(filter(lambda x: x % 3 == 0, lst))
print(nums([3, 15, 22, 46, 21, 89, 9]))

#9
def num_range(lst: int) -> list:
    return list(filter(lambda x: x in range(5,10), lst))
print(num_range([12, 5, 22, 1, 9, 10, 7]))

#10
def words(lst:str) ->list:
     return list(filter(lambda x: x.endswith("o"), lst))
print(words(["Hello", "ali","Arizona","Pyhton","trololo"]))

# (ДОП ЗАДАНИЯ)
#1
def new_line(aray: str) -> list:
    return [word for word in aray if len(word) > 5]
print(new_line(["hello", "I'm", "Pyhton", "thanks", "assistance"]))

#1 (другой вариант решения)
array = ["hello", "I'm", "Pyhton", "thanks", "assistance", "Global"]
print([word for word in array if len(word) > 5])

#2
dict_2 = dict()
dict_1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
for (k, v) in dict_1.items():
    dict_2[k] = k
    if v % 2 != 0:
        dict_2[k] = v ** 2
print(dict_2)

#2
a = {k: k if k % 2 == 0 else k ** 2 for k in range(1, 11)}
print(a)


#4
a = [i **3 if i ** 3 % 4 != 0 else "FOUR" for i in range(1,11)]
print(a)

