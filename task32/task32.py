# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


n = int(input('Введите кол-во чисел: '))
list_1 = [randint(1, 50) for i in range(n)]
print(list_1)
min = int(input('введите минимальное значение: '))
max = int(input('введите максимальное значение: '))
for i in range(n):
    if min < list_1[i] < max:
        print(i)
        