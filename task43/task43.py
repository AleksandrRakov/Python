from random import randint


n = int(input('Введите кол-во чисел: '))
list_1 = [randint(1, 20) for i in range(n)]
print(*list_1)
result = {}
for element in list_1:
    if element  in result:
        result[element] += 1
    else:
        result[element] = 1
print(sum([i//2  for i in result.values()]))