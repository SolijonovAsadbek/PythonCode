import json

from pprint import pprint as pp

#
# with open('humo_json.json', 'rb') as file:
#     data = json.load(file)
# pp(data)

# x = 12
# # print("x: ", x, type(x))
# x_json = json.dumps(x)
# # print('x_json: ', x_json, type(x_json))
# x_unpack_json = json.loads(x_json)
# print('x_unpack_json:', x_unpack_json, type(x_unpack_json))

# JSON ma'lumot turini indentatsiya bilan saqlash.
# my_dict = {"name": 'Jason', "age": 12, "family": False, "school": 29, 'children': ['ali', 'vali', 'shoptali']}
# my_dict_json = json.dumps(my_dict, indent=4)
# my_dict_unpack = json.loads(my_dict_json)
# pp(my_dict_unpack)


# Python ma'lumot turini JSON file ga o'tkazish
my_dict = {"name": 'Jason', "age": 12, "family": True, "school": 29, 'children': ['Ali', 'Bobur', 'Toshmat']}

with open('person.json', 'w') as file:
    json.dump(my_dict, file, indent=4)

with open('person.json', 'r') as file:
    data = json.load(file)
print(data)
print(f"ismi: {data['name']}\n"
      f"yoshi: {data['age']}\n"
      f"Farzandlari: {','.join(data['children'])}\n"
      f"Oilasi: {('Oila qurgan' if data['family'] else 'Oila qurmagan.')}")
