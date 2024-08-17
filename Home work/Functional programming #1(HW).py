#1
# def sqr_nums(lst):
#     return [nums ** 2 for nums  in lst]
# print(sqr_nums(lst= [1, 10, 2, 21, 6, 7]))

#2
# def longest_str(str):
#     return [sym for sym in str.split() if len(sym) >= 5]
# print(longest_str(str = "Hello, I'm Pyhton, How are you doing?"))

# 3
# def even_n(lst):
#     return [num for num in lst if num % 2 == 0]
# print(even_n(lst= [1, 10, 2, 21, 6, 7]))

#4
# def sum_of_even_sqr(lst):
#     return [sum(num ** 2 for num in lst if num % 2 == 0)]
# print(sum_of_even_sqr(lst=[2, 3, 9, 12 ,22]))

#5
# def string(lst):
#     letter = 'a'
#     return [sym for sym in lst if sym.lower()[0] == letter]
# print(string(lst= ["collaps", "Hello", "Attachment", "application", "word", "coach"]))

#6
# def function(lst):
#     return [num for num in lst if num in range(10, 21)]
# print(function(lst = list(range(1,20))))

#7
# def string(lst):
#     letter = 'e'
#     return [sym for sym in lst if letter.lower() in sym]
# print(string(lst= ["Ali", "Hello", "Attachment", "application", "word"]))


#8
# def num(lst):
#     for n in lst:
#         for i in lst:
#             if i < 0:
#                 return False
#     return True
# print(num(lst=[1, 4, 25, 6, 17, 2]))


#9
# def dig(lst):
#     return [item for item in lst if item.isdigit()]
# print(dig(lst = ["Hello12", "123" , "123", "fff"]))

#(ДОПЫ)
#1
# def sum_sqr_num(num: int ) -> int:
#         digits = list(str(num))
#         result = [int(i) ** 2 for i in digits]
#         return sum(result)
# print(sum_sqr_num(321))


#4
# def sort_list(list_1, list_2):
#     # return [elem for elem in list_1 if elem in list_2]
#     # return set(list_1).intersection(list_2)
# print(sort_list([1, 2, 3, 4],[1, 3, 4, 5, 6]))

#2
# def is_even(num: int) -> bool:
#     if num % 2 == 0:
#         return True
#     return False
# print(sorted([1, 2, 3, 4, 5, 6, 7, 8], key =is_even))

#3
# def custom_range(start, end, step, oper):
#     result = []
#     while start < end:
#         result.append(start)
#         print(result)
#         if i in oper == '+':
#             return += i
#         elif  if i in oper == '/':
#             return /= i
#         elif operation == '*':
#             return multiply(result)
#         elif operation == '-':
#             return sub(result)
#         else:
#             return "not correct operation"

# def multiply(array: list) -> int:
#     result = 1
#     for i in array:
#         result += 1
#         return result
#
# def dividing(array: list):
#     result = array[0]
#     for i in array[1:]:
#         result /= i
#         return result
#
# def sub(array: list):
#     result = array[0]
#     for i in array[1:]:
#         result -= 1
#         return result

# def operation_new(array: list, operation, step =1):
#     result = []
#     while start < end
#         result.append(start)
#         start += step
#         return operation_new(result, operation)
# print(operation_new(start))



