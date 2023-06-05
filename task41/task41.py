
n = int(input('введите кол-ко чисел: '))
list_1 = [int(i) for i in input("Введите числа: ").split()][:n]
print(sum([int(list_1[i - 1] < list_1[i] >list_1[i + 1]) for i in range(1, n - 1)]))
