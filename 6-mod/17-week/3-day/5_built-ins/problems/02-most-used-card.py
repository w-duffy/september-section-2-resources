# Given a list of dictionaries representing credit cards, sort the list in
# descending order according to the `num_users` property. Do the sort out-of
# place without mutating the original list, using the `sorted` built in
# function, and then return only the company names in a list, in the correct
# sorted order.

cards = [
    {
        "company": "Wells Fargo",
        "card_name": "Active Cash",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 200,
        "num_users": 20,
    },
    {
        "company": "Chase",
        "card_name": "Sapphire Preferred",
        "annual_fee": 95,
        "intro_reward_type": "points",
        "intro_reward_amount": 60000,
        "num_users": 54,
    },
    {
        "company": "Citi",
        "card_name": "Diamond Preferred",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 150,
        "num_users": 13,
    },
]

#! --------------------------------------------------------------------
# *                             Using Built ins
#! --------------------------------------------------------------------


# def sort_cards(card_list):
#     sorted_cards = sorted(card_list, key=lambda card: card["num_users"], reverse=True)
#     return list(map(lambda card: card["company"], sorted_cards))


def sort_cards(card_list):
    return list(
        map(
            lambda card: card["company"],
            sorted(card_list, key=lambda card: card["num_users"], reverse=True),
        )
    )


#! --------------------------------------------------------------------
# *                            Single Helper
#! --------------------------------------------------------------------

# def more_users(card):
#     return card["num_users"]


# def sort_cards(card_list):
#     return [card["company"] for card in sorted(cards, key=more_users, reverse=True)]


#! --------------------------------------------------------------------
# *                           Multi Helpers
#! --------------------------------------------------------------------

# def sorter(card):
#     return card["num_users"]


# def get_companies(card):
#     return card["company"]


# def sort_cards(card_list):
#     sorted_info = sorted(card_list, key=sorter, reverse=True)
#     only_company_names = map(get_companies, sorted_info)
#     return list(only_company_names)


# def sort_cards(card_list):
#     return list(map(get_companies, sorted(card_list, key=sorter, reverse=True)))


# one_line_sort_cards = lambda card_list: list(
#     map(
#         lambda card: card["company"],
#         sorted(card_list, key=lambda card: card["num_users"], reverse=True),
#     )
# )

# def sort_cards(card_list):
#     pass


print(sort_cards(cards))  # ['Chase', 'Wells Fargo', 'Citi']
