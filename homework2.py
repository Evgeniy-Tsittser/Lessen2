name_doc = 'Чек'
print(name_doc)
name_produkt = 'Черешня'
print(name_produkt)
ves = float(input('Вес, кг: '))
match = float(input('Цена, руб/кг: '))
cost = ves * match
print('Сумма: ', float(cost))
cash = float(input('Получено, руб.: '))
change = cash - cost
print('Ваша сдача: ', change)
print('Всего доброго!')

