menu = {'pizza': 'Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy',
        'salad': 'Caesar salad, Green salad, Tuna salad, Fruit salad',
        'soup': 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'}

request = input()
print(menu.get(request, "Sorry, we don't have it in the menu"))
