import math
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

D = b*b + 4*a*c
if D > 0:
    x1= ((-b + math.sqrt(D))/2*a)
    x2= ((-b - math.sqrt(D))/2*a)
    print(x1, x2)
elif D == 0:
    x1=((-b)/2*a)
    print(x1)
else:
    print ("Корней нет")