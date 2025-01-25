# Say you took a survey of your class of all the phones, and you want to get all
# the unique phone models.

# First, write a function `get_unique_models` that filters out duplicates of a
# given model. Assume that brands and models are one-to-one, meaning there won't
# be two brands that have same model name.

# Then, write a function `map_to_names` that returns a list of just the model
# names given the list of phones.

phones = [
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "alpine green"
    },
    {
        "brand": "Samsung",
        "model": "Galaxy S22+",
        "cost": 999,
        "color": "black"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "kinda coral"
    },
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "gold"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "stormy black"
    }
]

# Write your code here.
#!!ADD
def get_unique_models(phone_list):
    pass

def map_to_names(phone_list):
    pass
#!!END_ADD
#!!START SILENT
# Note, other solutions are possible!

def get_unique_models(phone_list):
    seen = []
    return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)

def map_to_names(phone_list):
    return list(map(lambda phone: phone['model'], phone_list))
#!!END

unique_models = list(get_unique_models(phones))
print(unique_models)                # iPhone 13 Pro, Galaxy S22+, Pixel 6 (dictionaries)
print(map_to_names(unique_models))  # iPhone 13 Pro, Galaxy S22+, Pixel 6