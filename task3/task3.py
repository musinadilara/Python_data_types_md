list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

similar = []
different = []
for i_1 in list1:
    if i_1 in list2:
        similar.append(i_1)
        list2.remove(i_1)
    else:
        different.append(i_1)


print('Элементы, которые встречаются в обоих списках:',*similar)
print('Элементы, которые уникальны для первого списка:',*different)
print('Элементы, которые уникальны для второго списка:',*list2)
