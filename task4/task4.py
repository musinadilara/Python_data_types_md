items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]

products = {}

for item in items:
    name, typ = item
    if typ in products:
        products[typ].append(name)
    else:
        products[typ] = [name]
print('Продукты по катерогиям :',products)