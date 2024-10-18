import math
def square(side):
     return math.ceil(side*side)
num_side = int(input("Введите число:  "))
print(f"Площадь квадрата: {square(num_side)}")