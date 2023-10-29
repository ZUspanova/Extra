a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a > b and a > c and b>c:
    print (a,b,c)
elif b > a and b > c and a>c:
    print (b,a,c)
elif c > a and c > b and b>a:
    print (c,b,a)