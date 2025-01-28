# Python Dictionaries.
# student_info ={
#     "Nahid":{
#         "name":"nahid",
#         "Location": "kallyanpur",
#         "Home": "munshiganj",
#         "study": "10",
#         "subject":"commarce",
#         "School":"hakkani mission school",
#     },
#     "kobir":{
#         "name":"nahid",
#         "Location": "kallyanpur",
#         "Home": "munshiganj",
#         "study": "12",
#         "subject":"science",
#         "School":"mohammadpur govt school",
#     },
#     "Age": 13250
# } 

# # PYTHON change item.
# student_info["Age"]=2005
# print(student_info)
# # update values 
# student_info.update({"Age":6580})
# print(student_info["Age"])
# # python remove method.
# # student_info.pop("kobir")
# # print(student_info)
# # student_info.pop("Age")
# # print(student_info)
# # .student_info["Kobir"]
# del student_info["kobir"]
# print(student_info)

# student_info.clear()
# print(student_info)


# dictinary type
# student_info ={
#     "Nahid":{
#         "name":"nahid",
#         "Location": "kallyanpur",
#         "Home": "munshiganj",
#         "study": "10",
#         "subject":"commarce",
#         "School":"hakkani mission school",
#     },
#     "kobir":{
#         "name":"kobir",
#         "Location": "kallyanpur",
#         "Home": "munshiganj",
#         "study": "12",
#         "subject":"science",
#         "School":"mohammadpur govt school",
#     },
#     "Age": 13250
# } 
# # for x in student_info:
# #     print(x)
# # for i in student_info.values():
# #     print(i)
# # for t in student_info.keys():
# #     print(t)
# # for item in student_info.items():
# #     print(item)

# # python copy type
# info_of_weeding = {
#     "sum" : 150,
#     "sum 1" : 200,
#     "sum 2" : 250

# }
# # a = info_of_weeding.copy()
# # print(a)
# k = dict(info_of_weeding)
# print(k)
# Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.get("model"))