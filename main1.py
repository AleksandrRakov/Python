# n = 5
# print(n)



# n = "dfddf\"gfg"
# print(n)



# print(5,6,5)


# # print(5,6,9)

# print(5,6)


# """print(5,6,5)
# print(5,6,5)"""



# print(5,6,5)



# a = 5
# b = 5.89
# c = "hello"
# print(a,b,c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))




# print("Введите первое число: ")
# a = input()
# print(a)



# print("Введите первое число: ")
# a = input()

# b = input(" Введите второе число: ")

# print("Введите первое число: ")
# a = input()

# b = input(" Введите второе число: ")
# print (a, " + ", b, " = ",a + b)



# c =  5.89
# print(c)
# n = int(c)
# print(n)



# c =  5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# print("Введите первое число: ")
# a = int(input())

# b = int(input(" Введите второе число: "))
# print (a, " + ", b, " = ",a + b)



# a = 5.8989
# b = 6.89898
# print(round(a*b,3))




# a = 1 < 3 < 5 < 10
# print(a)




# username = input("Введите имя: ")
# if username == "Маша":
#     print("Ура, это же Маша!")
# elif username == "Марина":
#     print ("Я так ждал вас, Марина!")
# elif username == "Ильнар":
#     print("Ильнар - топ!")
# else:
#     print("Привет,",username)    



# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i = i + 1
# else:
#     print("( Пожалуй")
#     print("хватит )")    
# print(i)



# a = "qwerty"
# for i in a:
#     print(i)





# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)     

# text = "Сьешь  еще что - НибудЬ вкуСноЕ наВерНое"
# print(len(text))
# print("еще" in text)
# print(text.lower())
# print(text.upper())
# print(text.replace("еще", "ЕЩЕ"))




# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]

# print(len(list_1))
#print(list_1[-2])  #при минусе работает в обратном порядке




# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) #добавляет какой-то элемент в конец списка пример "8"
# print(list_1)
# list_1.append(85)
# print(list_1)




# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)




# list_1 = [12, 7, -1, 21, 0]
                      # # a = list_1.pop()---- в этом случае последний элемент массива кладеться в "а"
                      # # print(a)
# print(list_1)
# print(list_1.pop())  #-----в этом случае идет удаление последнего элемента из массива
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)



# Удаление конкретного элемента
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.pop(0))
# print(list_1)




# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# list_1.insert(2, 11)   #--добавили "11" на место 2-го элемента
# print(list_1)




# t = ()

# print(type(t))

# t = (1, 5, 3,)
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)  # кортеж
# print(type(v))

# a, b, c = v  #--распаковка кортежа
# print(a, b, c)




# t = (1, 2, 3, 5,)
# print(t)
# for i in range(len(t)):
#     print(t[i])



#Совари

def sum(n):
    summa =0
    for i in range(1,n):
        print(i)
        summa +=i
    print(summa)
sum(6)
