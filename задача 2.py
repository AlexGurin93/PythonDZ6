# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
a = eval('2+2')
print(a)

b = eval('1+2*3')
print(b)

c = eval('1-2*3')
print(c)
print('----------')
a1 = (lambda x, y: x + y)(2, 2)
print(a1)
b1 = (lambda x, y, c: x + y * 3)(1, 2, 3)
print(b1)
c1 =(lambda x, y, c: x - y * 3)(1, 2, 3)
print(c1)
