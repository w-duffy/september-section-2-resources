# def my_func():
#   """
#   This is just to show help working
#   I can document a function
#   others can call help or hover
#   """
#   return "hello world"


# # Conditionals

# name = 'Tony'
# name2 = 'Bob'

# new_list = []




# # if name == 'Tony' and not name2 == "Will":
# #   print('Hello Tony')
# # elif name == 'Peter':
# #   print('Hello Peter')
# # else:
# #   print('Hello')

# # dict_items([('key', 'value2')])

# # Loops


# lst = [1,2,3]
# lst2 = ["review","another one"]

# # lst[0] = 12351235

# # print(lst)


# # my_dict = {"spots": [1,2,3], "Reviews": [1,2,3,4]}

# # print(my_dict["spots"])

# # my_dict["spots"] = "new value"

# # print(my_dict["spots"])

# # print(my_dict is my_dict)


# ## For loop

# # for num in lst:
# #   print(num)

# # for letter in my_string:
# #   print(letter)

# # for k, v in my_dict.items():
# #   print(k, v)


# # help(my_dict.items())

# lst = ["hello", "world", "moon"]
# # print(range(len(lst)))

# # for index in range(len(lst)):
# #   print(lst[index], index)
# my_dict = {"key": "value", "key2": "value2"}



# my_string = "some string"
# for key, val in my_dict.items():
#   print(True is True)


# ## While loop

# index = 0
# while index < len(lst):
#   print(lst[index])
#   index += 1






lst = [1,2,3]

lst.extend()
# # b = "5"
# # b = 0
# # b = 5

try:
    print(a / 0)
except ZeroDivisionError:
    print("did i get hit?")
except (TypeError, NameError) as e:
    print("ERROR!", e)
    a = 100
    print(a)
finally:
    print("Finally...")
