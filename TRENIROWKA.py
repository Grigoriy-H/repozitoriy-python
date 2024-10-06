x = 1258
print(x)

name = "Григорий"
print("Как дела!? " + name)
x = False
print(x)
r = True
print(r)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(numbers[7])
print(numbers[0])
print(numbers[-1])
print(numbers[-10])
print(numbers[10])

spisok = []
x = len(spisok)
print(x)

dninedeli = [
            "понедельник",
            "вторник",
            "среда", 
            "четверг", 
            "пятница", 
            "суббота", 
            "воскресение"
            ]
R = len(dninedeli)
print(R)                     # "len" - выводим на печать число элементов в списке!

W = dninedeli[0]       # создали переменную и напечатали день недели согласно индекса "0"
print(W)                     # понедельник
V = dninedeli[4]
print(V)
G = dninedeli[-6]
print(G)

#            ФУНКЦИЯ  - def

def matematika(a, b):  # - объявление функции
    print(a)
    print(b)
    sum = 200+300
    return sum 


# упрощение функции
print(dninedeli[-7])

# ФУНКЦИЯ
#   def            объявление функции

def Matematika(a, b, c):   # -  меня вызвали
    print(a+b+c)                     
Matematika(7,14,21)
Matematika(1,4,14)
Matematika(21,574,241)
Matematika(10,531,247)
Matematika(1100,54,248)
#
x = Matematika(7,14,21)
x = Matematika(1,4,14)
x = Matematika(21,574,241)
x = Matematika(10,531,247)
x = Matematika(1100,54,248)
print(x)

def print_number(num):
    print(num, end="")


print_number(8)
print_number(8)
print_number(0)
print_number(0)
print_number(5)
print_number(5)
print_number(5)
print_number(3)
print_number(5)
print_number(3)
print_number(5)




def h(name):
     print("Привет мой дорогой друг " + name)
h("Владимир")
h("Сергей")
h("Иван")
h("Стас")

def kalkulator(x,y):        #Умножение
    return x*y
Q = kalkulator(4,5)
print(Q)

def kalkulator(x,y):        #Деление
    return x/y
Q = kalkulator(4,5)
print(Q)

def kalkulator(x,y):       
    return x/y
Q = kalkulator(40,5)
print(Q)

# Видимость переменной

P = 1777777777          # Внешняя переменная
def pechat():
    print(P)
pechat()

def printlocal():       
    O = 585              # Переменная внутри функции (Внутренняя переьенная)
    print(O)
printlocal()

                                        # CТЕК ВЫЗОВОВ

def funcalA():
    print("Начали выполнять А")
    funcalB()
    print("Закончили выполнять А")

def funcalB():
    print("Начали выполнять B")
    funcalC()
    print("Закончили выполнять B")

def funcalC():
    print("Начали выполнять C")
    funcalD()
    print("Закончили выполнять C")

def funcalD():
    print("Начали выполнять D")
    print("Закончили выполнять D")

funcalA()   

first_name = input()
last_name = input()
print("Вас зовут:", last_name, first_name)




def print_number(num):
    print(num, end="")
print_number(8)
print_number(8)
print_number(0)
print_number(0)
print_number(5)
print_number(5)
print_number(5)
print_number(3)
print_number(5)
print_number(3)
print_number(5)
