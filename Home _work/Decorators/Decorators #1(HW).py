#1
# import time
# def decorator(func):
#     def wrapper():
#         print("Loading ....")
#         time.sleep(3)
#         func()
#         print("Loading is done!")
#     return wrapper()
#
# @decorator
# def something():
#     return print([num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0])

# 2
# from datetime import datetime
# def logger(func):
#     def wrap():
#         start = datetime.now()
#         print("Начало процесса :", f'{start}')
#         func()
#         count = datetime.now() - start
#         print(f"Время выполнения {count} функции {func.__name__}")
#         print("Время окончания процесса: ", datetime.now())
#     return wrap
#
# @logger
# def get_list_1():
#     return [i for i in range(100000000)]
#
#
# print(get_list_1())

#3
import time
# def decorator(func):
#     def wrapper(user_type):
#         if user_type in ["admin", "auth_user"]:
#             func(enter)
#             return f"Hello {user_type}, we glad to see you"
#         return f'Hello {user_type}, you cant enter'
#     return wrapper
#
# @decorator
# def enter(user_type):
#     print("Hello please name your self")
#
#
# print(enter("admin"))
# print(enter("auth_user"))
# print(enter("user"))


#4
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         dict_1 = func.__annotations__
#         if len(kwargs):
#             for key in kwargs:
#                 if type(kwargs[key]) != dict_1[key]:
#                     return False
#                 dict_1.popitem(key)
#         if not len(dict_1):
#             return True
#         for k in range(len(dict_1)):
#             if type(args[k]) != dict_1.values()[k]:
#                 return False
#         return True
#     return wrapper
#
#
# @decorator
# def bar(array_1: int, array_2: str):
#     nums = array_2.split(",")
#     nums_int = [int(x) for x in nums]
#     nums_int.insert(array_1, 12)
#     print(nums_int)
#
#
# print(bar(array_1=12, array_2="2,4,5"))


#4 (в классе)
# import time
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         ann = func.__annotations__
#         if len(kwargs):
#             for key in kwargs:
#                 if type(kwargs[key]) != ann[key]:
#                     return False
#                 ann.popitem(key)
#         if not len(ann):
#             return True
#         for k in range(len(ann)):
#             if type(args[k]) != list(ann.values())[k]:
#                 return False
#             return True
#     return wrapper
#
# @decorator
# def something(x: int, y: str, z: float):
#     time.sleep(2)
#
# print(something(1,"2",3.0))

#5
from time import sleep

# def cache_three(func):
#     counter, cache = 0, dict()
#     def wrap(x):
#         nonlocal counter
#         counter += 1
#         if counter in range(1, 5) and cache:
#             return cache['cache']
#         cache['cache'], counter = func(x), 0
#         return cache['cache']
#     return wrap
#
# @cache_three
# def difficult_operation(x: int):
#     sleep(1.5)
#     return x ** 2
#
# print(difficult_operation(4))
# print(difficult_operation(21))
# print(difficult_operation(36))
# print(difficult_operation(4))
# print(difficult_operation(2))
# print(difficult_operation(10))































