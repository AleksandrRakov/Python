n = int(input("Введите кол-во арбузов: "))
max = 0
min = 1001
for i in range(n):
    m = int(input("Введите массу арбуза: "))
    if max < m:
        max = m
    if min > m:
        min = m
print(min,max)
