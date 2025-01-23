# ## Pargs / Args / Kwargs


# # def my_func(first_param, *args):
# #     print(first_param, "\n", args)

# # def my_func(postitional_arg, *args, **kwargs):
# #     print("first arg: ",postitional_arg)
# #     print("args: ", args)
# #     print("kwargs: ", kwargs)


# # # my_func("taco", "second_default_val", kwarg_word="world", first_word="hello" )
# # my_func("taco", "second_default_val" )


# ## lambda functions


# # anon_func = lambda x, y: x + y
# # print(anon_func(1, 2))


# #  let something = true ? 1 : 2
# # [expression (optional if -> else) for element in iterable (optional if expression)]

# this_lst = [0, 1, 2, 3]

# add_ten_yes_or_no = False

# if True:
#     add_ten_yes_or_no = True

# # new_lst = []

# # if add_ten_yes_or_no:
# #     for el in this_lst:
# #         if el != 2:
# #             new_lst.append(el + 10)
# # else:
# #     for el in this_lst:
# #         if el != 2:
# #             new_lst.append(el - 10)


# # # [expression (optional if -> else) for element in iterable (optional if expression)]

# new_lst_false = [el + 10 for el in this_lst if el != 2]

# add_ten_yes_or_no = True



# new_lst_true = [el + 10 if True else el - 10 for el in this_lst]


# # # print("true: ", new_lst_true)
# # print("false: ", new_lst_false)

# # [expression  for element in iterable ]
# #

# # new_list_2 = []

# # for el in this_lst:
# #     if el != 2:
# #         new_list_2.append(el + 10)

# # print(this_lst)
# # print(new_lst)
# # print(new_lst is this_lst)

# # for el in lst:
# #     new_lst.append(el + 1)


# # let newArr = arr.map(el => el + 1)


# # el => el + 1
# # new_list = list(map(lambda x: x + 1, lst))


# # print(new_list)


# all_posts = [
#     {
#         "id": 1,
#         "text": "Just deployed my first Python app! #coding #python #developer",
#         "likes": 42,
#         "tags": ["coding", "python", "developer"],
#         "timestamp": "2024-03-15 14:30:00",
#         "comments": [
#             {"user": "zav", "text": "Great job!"},
#             {"user": "will", "text": "Python is sweet"},
#             {"user": "zav", "text": "What framework did you use?"},
#             {"user": "will", "text": "Follow the Zen of Python"},
#             {"user": "alexi", "text": "Very pythonic!"},
#         ],
#     },
#     {
#         "id": 2,
#         "text": "Just deployed my first Python app! #coding #python #developer",
#         "likes": 42,
#         "tags": ["coding", "python", "developer"],
#         "timestamp": "2024-03-15 14:30:00",
#         "comments": [
#             {"user": "zav", "text": "Great job!"},
#             {"user": "will", "text": "Python is sweet"},
#             {"user": "zav", "text": "What framework did you use?"},
#             {"user": "will", "text": "Follow the Zen of Python"},
#             {"user": "alexi", "text": "Very pythonic!"},
#         ],
#     },
# ]

# # post = {
# #     "id": 1,
# #     "text": "Just deployed my first Python app! #coding #python #developer",
# #     "likes": 42,
# #     "tags": ["coding", "python", "developer"],
# #     "timestamp": "2024-03-15 14:30:00",
# #     "comments": [
# #         {"user": "zav", "text": "Great job!"},
# #         {"user": "will", "text": "Python is sweet"},
# #         {"user": "zav", "text": "What framework did you use?"},
# #         {"user": "will", "text": "Follow the Zen of Python"},
# #         {"user": "alexi", "text": "Very pythonic!"},
# #     ],
# # }
# all_posts_filtered = [
#     comment
#     for el in all_posts
#     for comment in el["comments"]
#     if comment["user"] == "will"
# ]

# print(all_posts_filtered)

# new_lst = []
# for post in all_posts:
#     for comment in post["comments"]:
#         if comment["user"] == "will":
#             new_lst.append(comment)

# print("\n", new_lst)

# # all_posts_filtered = [comment for post in all_posts for comment in post["comments"] if comment["user"] == "will"]

# # print("ALL POST FILTERED: ", all_posts_filtered)
# ## do a list comp and return comments from the post where the user is will
# # # [expression (optional if -> else) for element in iterable (optional if expression)]


# # wills_comments = [comment
# #                   for comment in post["comments"]
# #                   if comment["user"] == "will"]

# # print(wills_comments)
# # for comment in post["comments"]:
# #     # print("comment: ", comment["user"])
# #     user_name = comment["user"]
# #     if user_name == "will":
# #         wills_comments.append(comment)

# # print("Wills comments: \n\n", wills_comments, "\n")


# # Tuples
# # my_tupe = ("hello", "world", 1, 2)

# # new_val, is_world, num1, num2 = my_tupe
# # # print(f"new val! {new_val}")

# # def my_funky_func():
# #     food = "tacos"
# #     day = "today"
# #     some_num = 123
# #     return (food, day, some_num)

# # print(my_funky_func())
# # not_called_food, day, something  = my_funky_func()
# # print(f"what does this print: {not_called_food}")


# # dupe_list = [1,1,3,3,5,6]
# # print(list(set(dupe_list)))


# # # my_tupe[0] = "goodbye" # Error
# # for t in my_tupe:
# #     print(t)

# #################################################################################################
# # Sets
# new_set = {"hi"}
# print(new_set)

lst = [1,1,1,3,5,6,2,6,2,3]
# print(list(set(lst)))


def route_handler():
    return {"Spots": [{"id": "1"},{"id": "2"}]}

# all_tags = {"python", "javascript", "coding", "developer", "python"}  # notice duplicate "python"
# print(all_tags)
# # all_tags.


# #################################################################################################

# # num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # """
# # Use a set to remove duplicate elements from a list
# # """


# #################################################################################################

# # tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# # # """
# # # Convert a tuple to a list, and back to a tup
# # # """


# #################################################################################################

# lst = ["hello", "world", "goodbye", "moon"]
# # """
# # Use enumerate to print the elements and indices of a list
# # """

# # [(0, 'hello'), (1, 'world'), (2, 'goodbye'), (3, 'moon')]


# #################################################################################################

# # # """
# # # Write a function that takes in a list of lists where elements are numbers and returns
# # # a new list of lists where every element in the new list is 10
# # # greater than the corresponding element in the original list.
# # # """
# # two_dimensional_list = [[1, 2], [4, 5, 6], [7, 8, 9, 10]]

# string_itr  = "hello"

lst = [1,2,3]


# el => el + 10
# print(list(map(lambda x: x + 10, lst)))

# def only_return_two(num):
#     return num == 2
#         # return num

# # print(only_return_two(1))

# # print(list(filter(only_return_two,lst)))
# print(list(filter(lambda x: x == 2,lst)))



# filter()




# two_dimensional_list = [[1, 2], [4, 5, 6], [7, 8, 9, 10]]
# some_lst = [1,2,3]

#     # return_lst = []
#     # for inner_lst in lst:
#     #     nested_return_lst = []
#     #     for num in inner_lst:
#     #         nested_return_lst.append(num+ 10)
#     #     return_lst.append(nested_return_lst)
#     # return return_lst

# nested_lst =  [7, 8, 9, 10]
# comp_res = [el + 10 for el in nested_lst]

# # print(comp_res)

# def get_new_list(lst):
#     # access inner elements and add 10 to them
#     return [[el + 10 for el in nested_lst] for nested_lst in lst]


# print(get_new_list(two_dimensional_list))  # [[11, 12], [14, 15, 16], [17, 18, 19, 20]]

# #################################################################################################

# # """
# # Use a list comprehension
# # """

def add_ten(num):
    return num + 10
print(list(map(add_ten, lst)))



two_dimensional_list = [[1, 2], [4, 5, 6], [7, 8, 9, 10]]

value = "hi" if False else "cat" if False else "dog"
print(value)

def get_new_list(lst):
    # access inner elements and add 10 to them
    # return [[el + 10 for el in nested_lst] for nested_lst in lst]
    return [list(map(add_ten, nested_lst)) for nested_lst in lst]

print(get_new_list(two_dimensional_list))
# def get_new_list_using_list_comp(lst):
#     pass


# print(get_new_list_using_list_comp(two_dimensional_list))  # [[11, 12], [14, 15, 16], [17, 18, 19, 20]]
# #################################################################################################


# # """
# # Use map with a list comprehension
# # """
# # # print("Just testing the map", new_list) # prints [10, 12]


# two_dimensional_list = [[1, 2], [4, 5, 6], [7, 8, 9, 10]]


# # print(get_new_list(two_dimensional_list))  # [[11, 12], [14, 15, 16], [17, 18, 19, 20]]

# #################################################################################################

# # """
# # # Write a function that takes in a dictionary and returns
# # # a new dict only if the person lives in EST
# # """


# dict1 = {"will": "CST", "sam": "EST", "zaviar": "PST", "alex": "EST"}


dict1 = {"will": "CST", "sam": "EST", "zaviar": "PST", "alex": "EST"}


# def filtered_dict(some_dict: dict):
#     # iterate through the dictionary and check values
#     return_dict = {}
#     for key, val in some_dict.items():
#         if val == "EST":
#             # print(key, "val: ", val)
#             return_dict[key] = val

#     return return_dict


# def filtered_dict_comp(some_dict: dict):
#     return {key: val for key, val in some_dict.items() if val == "EST"}

# print(filtered_dict_comp(dict1))

# #################################################################################################


# # """
# #  Use a dictionary comprehension to create a new dictionary where returns
# # we only have people that live in EST
# # """

# dict1 = {"will": "CST", "brandon": "EST", "zaviar": "PST", "alex": "EST"}


# def filter_dict(a_dict: dict):
#     pass


# # print(filter_dict(dict1))
