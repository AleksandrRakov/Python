# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника)

a = int(input("Введите размер шоколадки длинна: "))
b = int(input("Введите размер шоколадки ширина: "))
c = int(input("Сколько долек хотите отломить: "))
if c % a == 0 or c % b == 0:       # a * b >= c and (c % a == 0 or c % b == 0 )-- пример с семинара
    print("yes")
else:
    print("no")

