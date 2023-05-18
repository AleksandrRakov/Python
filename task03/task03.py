import math


n = int(input("Кол-во учеников в 1-ом кабинете: "))
m = int(input("Кол-во учеников в 2-ом кабинете: "))
a = int(input("Кол-во учеников в 3-ом кабинете: "))
# result = n // 2 + n % 2 + m // 2 + m % 2 + a // 2 + a % 2 
# print(result)


result = math.ceil(n / 2) + math.ceil(m / 2) + math.ceil(a / 2) 
print(result)
