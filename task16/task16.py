# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#  1 2 3 4 5
# 3
# -> 1

n = int(input('Введите количество чисел: '))
count = 0
x = [int(i) for i in input("Введите числа: ").split()]
b = int(input("Число поиска: "))
for i in range(n):
    if x[i] == b:
        count +=1   
print("Количество чисел: ",count)



