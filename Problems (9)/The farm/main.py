from collections import OrderedDict

cash = int(input())

prices = OrderedDict([('Chicken', 23),
                      ('Goat', 678),
                      ('Pig', 1296),
                      ('Cow', 3848),
                      ('Sheep', 6769)])

for animal, price in reversed(prices.items()):
    if price <= cash:
        n_bought = cash // price
        print(f'{n_bought} {animal.lower() + ("s" if n_bought > 1 and animal != "Sheep" else "")}')
        break
else:
    print('None')
