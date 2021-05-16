from typing import Text


stock = [
    {'name': 'iPhone Xs', 'stock': 24, 'price': 6500.0, 'recomended': ['Samsung 10S', 'Xiomi Mi10', 'iPhone 6']},
    {'name': 'Samsung 10s', 'stock': 88, 'price': 5000.0, 'discount': 5000},
    {'name': 'Xiomi Mi10', 'stock': 22, 'proce': 3000.0 },
]

print(type(stock[0]))

print(stock[0]['recomended'][1])

