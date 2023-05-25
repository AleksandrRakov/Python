# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

data = [int(i) for i in input("Введите числа: ").split()]
step = int(input("Введите кол-во сдвигов: "))
print(data)
step = step %len(data)
data = [data[i - step] for i in range(len(data))]
print(data)