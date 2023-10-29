a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a == b and a == c:
    print ("3")
elif a == b or a == c:
    print ("2")
else:
    print("0")