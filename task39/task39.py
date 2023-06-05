

n = int(input('Введите количество чисел: '))
x = [int(i) for i in input("Введите числа: ").split()]
m = int(input('Введите количество чисел: '))
x1 = [int(j) for j in input("Введите числа: ").split()]
for i in x:
   if i not in x1:
    print(i,end = ' ')          #print([i for i in x if i not in x1])



