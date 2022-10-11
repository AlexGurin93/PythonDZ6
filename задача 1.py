# Получение квадратов четных чисел из списка
data = [2, 3, 5, 9, 30]
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x ** 2), res))
print(res)
# Получение квадратов чисел из списка [1, 2, 3, 4, 5]
data = [1, 2, 3, 4, 5]
res = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(res)
