name_doc = 'Чек'
print(name_doc)
name_produkt = input('Ведите наименование товара: ')
print(name_produkt)
ves = float(input('Вес, кг: '))
match = float(input('Цена, руб/кг: '))
cost = ves * match
print('Сумма: ', float('%.2f' % cost))
cash = float(input('Получено, руб.: '))
change = cash - cost
print('Ваша сдача: ', float('%.2f' % change))
print('Всего доброго!')

