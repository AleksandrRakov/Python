a = int(input("Нахождение числа Фибоначи: "))
x = 0
x0 = 0
x1 = 1
i = 2
while x < a:
    x = x0 + x1
    x0 = x1
    x1 = x
    i += 1
    if x > a:
        i = 0 

if i == 0:
    print(-1)
else:
    print(i)