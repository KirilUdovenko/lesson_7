############## имопрт из файлов

# from lesson7_func import create_email
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print("!!!", e_mail)
#
# print(f"{__name__=}")

################
# import json
#
# def read_json(filename):
#     with open(filename, "r") as file:
#         some_data = json.load(file)
#         return some_data
#
# def write_json(filename):
#     with open(filename, "w") as file:
#         json.dump(some_data, file, indent=indent)
#
# # some_data = {"data": [12, 23, 34, 45],
# #              "date": "2021-10-30",
# #              "age": 50}
# # # print(some_data["age"])
#
# filename = "some_data.json"
# data = read_json(filename)
# print(data)
#
# # with open("some_data.json", "w") as file:
# #     json.dump(some_data, file, indent=4) # indent для читаемости кода в файле
# #
# # with open("some_data.json", "r") as file:
# #     some_data = json.load(file)
# # print(some_data["date"])
# import json
#
# my_list = [1, 2, 3]
#
# my_list_str_json = json.dumps(my_list)
# print(my_list_str_json, type(my_list_str_json))
#
# new_list = json.loads(my_list_str_json)
# print(new_list[0])

############ csv

# import csv
#
# filename = "test.csv"
#
# with open(filename, 'r', encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#     data = []
#
#     for row in reader:
#         data.append(row)
#
# print(data)
# data.append([10, 11, 12])
#
# with open("test_2.csv", 'w', encoding="utf-8") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(data)

######################
#
# price = 10
# assert price > 0, "Negative price"
# value_coef = 100 / price
# print(value_coef)

# регулярные выражения (введения)

import re

my_str = "c. 965 - c. 1040 BC"

numbers = re.findall(r"[0-9]+", my_str)
print(numbers)

