# Say you took a survey of your class of all the phones, and you want to get all
# the unique phone models.

# First, write a function `get_unique_models` that filters out duplicates of a
# given model. Assume that brands and models are one-to-one, meaning there won't
# be two brands that have same model name.

# Then, write a function `map_to_names` that returns a list of just the model
# names given the list of phones.

phones = [
    {"brand": "Apple", "model": "iPhone 13 Pro", "cost": 929, "color": "alpine green"},
    {"brand": "Samsung", "model": "Galaxy S22+", "cost": 999, "color": "black"},
    {"brand": "Google", "model": "Pixel 6", "cost": 599, "color": "kinda coral"},
    {"brand": "Apple", "model": "iPhone 13 Pro", "cost": 929, "color": "gold"},
    {"brand": "Google", "model": "Pixel 6", "cost": 599, "color": "stormy black"},
]

# my_set = set()
# print(my_set.add(1))  # None
# print(my_set.add(1) is None)  # True

#! --------------------------------------------------------------------
# *                        Using filter() + map()
#! --------------------------------------------------------------------


def get_unique_models(phone_list):
    model_set = set()
    return filter(
        lambda el: model_set.add(el["model"]) is None
        if el["model"] not in model_set
        else False,
        phone_list,
    )


def map_to_names(phone_list):
    return list(map(lambda el: el["model"], get_unique_models(phone_list)))


#! --------------------------------------------------------------------
# *                      Using loop + list comp
#! --------------------------------------------------------------------
# def get_unique_models(phone_list):
#     unique_phone_list = []
#     model_st = set()
#     #! iterate through the phone_list
#     for i in range(len(phone_list)):
#         phone = phone_list[i]
#         #! check if the phone model is already in the model_st
#         if phone["model"] not in model_st:
#             #! if not, add this phone in the unique list
#             unique_phone_list.append(phone)
#             #! add this unique model into the model_st
#             model_st.add(phone["model"])
#     return unique_phone_list


# def map_to_names(phone_list):
#     return [phone["model"] for phone in phone_list]


unique_models = list(get_unique_models(phones))
print(unique_models)  # iPhone 13 Pro, Galaxy S22+, Pixel 6 (dictionaries)
print(map_to_names(unique_models))  # iPhone 13 Pro, Galaxy S22+, Pixel 6
