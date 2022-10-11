# Выбрать из списка каждый третий элемент из исходного списка:
list_a = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
list_e = [x for i, x in enumerate(list_a, 1) if i % 3 == 0]
print(list_e)
# Из произвольного списка вывести кортеж четных элементов:
res = [(i, x) for i, x in enumerate(range(10)) if x % 2 == 0]
print(res)
#Объединяете отдельные элементы из каждой последовательности в кортежи
x = 'абв'
y = 'эюя'
zipped = zip(x, y)
print(list(zipped))