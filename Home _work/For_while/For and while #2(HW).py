#1
# string = ["12", "100km,", "New Line", "200", "pro1004ek", "randome"]
# only_digits = []
# for nums in string:
#     if nums.isdigit():
#         only_digits.append(nums)
# print(only_digits)


#3
# array = input("From keybord :")
# print([ord(letter) for letter in array])


#3**
# new_str = "is2 Thi1s T4est 3a".split()
# res = dict()
# for word in new_str:
#     for sym in word:
#         if sym.isdigit():
#             res[int(sym)] = word
# print(res)
#
# new_res = sorted(res.items())
# new_str = ""
# print(new_res)
# for item in new_res:
#     new_str += f"{item[-1]} "
# print(new_str)

#4
# dictionary_list = [{"Name": "Витя", "Age": 15, "Marks": [5, 7, 8]},
#                    {"Name": "Даша", "Age": 14, "Marks": [8, 6, 9]},
#                    {"Name": "Саша", "Age": 17, "Marks": [5, 6, 3]}]
# for i in range(len(dictionary_list) - 1):
#     for j in range(len(dictionary_list) - 1 - i):
#         if dictionary_list[j]['Age'] < dictionary_list[j + 1]['Age']:
#              dictionary_list[j], dictionary_list[j + 1] = dictionary_list[j + 1], dictionary_list[j]
# print(dictionary_list)





