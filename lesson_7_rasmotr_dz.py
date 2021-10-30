# persons = [{"name": "John", "age": 15},
#            {"name": "Kiril", "age": 25},
#            {"name": "Jackson", "age": 15},
#            {"name": "Jack", "age": 45}]

# ages = []
# names_lens = []
#
# for person_dict in persons:
#     ages.append(person_dict["age"])
#     names_lens.append(len(person_dict["name"]))
#
# print(ages, names_lens)
#
# min_age = min(ages)
# max_len_name = max(names_lens)
#
# for person_dict in persons:
#     if person_dict["age"] == min_age:
#         print(person_dict["name"])
#
# for person_dict in persons:
#     if len(person_dict["name"]) == max_len_name:
#         print(person_dict["name"])
#
# mean_age = sum(ages) / len(ages)
#
# print(mean_age)

#################

# my_dict_1 = {1: 1, 2: 2}
# my_dict_2 = {11: 11, 2: 22}
#
# result_1 = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
# print(result_1)
#
# result_2 = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
# print(result_2)
#
# result_3 = {key: my_dict_1[key] for key in my_dict_1 if key not in my_dict_2}
# print(result_3)
#
# result_4 = my_dict_1.copy()
# for key in my_dict_2:
#     if key in result_4:
#         result_4[key] = [result_4[key], my_dict_2[key]]
#     else:
#         result_4[key] = my_dict_2[key]
# print(result_4)

##############

# def change_list(my_list):
#     for index in range(0, len(my_list), 2):
#         my_list[index] = my_list[index][::-1]
#     return my_list
#
# my_list = ["qwe", "asd", "zxc", "123"]
# my_list = change_list(my_list)
# print(my_list)

############
# from random import randint, choice
# from string import ascii_lowercase as alphabet
#
# def create_email(domains, names):
#     name = choice(names)
#     domain = choice(domains)
#     number = randint(100, 999)
#     my_str = "".join([choice(alphabet) for _ in range(randint(5, 7))])
#     e_mail = f"{name}.{number}@sgdyyur.{domain}"
#     return e_mail
#
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print("------>>>", e_mail)
# >>>miller.249@sgdyyur.com



#####################################################
def sort_by_age(person_dict):
    age = person_dict["age"]
    return age

def sort_by_len_name(person_dict):
    name = person_dict["name"]
    return len(name)

def sort_by_len_name_and_age(person_dict):
    name = person_dict["name"]
    age = person_dict["age"]
    return len(name), age

persons = [{"name": "John", "age": 15},
           {"name": "Kiril", "age": 35},
           {"name": "Jackson", "age": 15},
           {"name": "Jack", "age": 45}]

sort_person_by_age = sorted(persons, key=sort_by_age)
print(sort_person_by_age)

sort_person_by_len_name = sorted(persons, key=sort_by_len_name)
print(sort_person_by_len_name)

sort_person_by_len_name_and_age = sorted(persons, key=sort_by_len_name_and_age)
print(sort_person_by_len_name_and_age)

# temperature = [-2, -4, -6, -3, 0, 3, 5, -1, -4]
#
# sort_temp = sorted(temperature, key=abs)
# print(sort_temp)

# words = ['ajsyg', 'asdd', 'qwe', '123', 'asdwqdfwq']
# sort_words = sorted(words, key=len)
# print(sort_words)
