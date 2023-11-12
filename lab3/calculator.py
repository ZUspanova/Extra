import math

def sum_numbers(a1,b1):            #сумма
    c = a1 + b1
    print ("Answer a+b: ", c)
    return c

def difference_numbers(a1,b1):        #разница
    c = a1 - b1
    print ("Answer a-b: ", c)
    return c

def division_numbers(a1,b1):          # деление
    c = a1 / b1
    print ("Answer a/b: ", c)
    return c

def multiplication_numbers(a1,b1):    #умножение
    c = a1 * b1
    print ("Answer a*b: ", c)
    return c

def degree_numbers(a1,b1):           #возведение в степень
    c = a1 ** b1
    print ("Answer a**b: ", c)
    return c

print ('''Available options: 
1. a+b
2. a-b
3. a/b
4. a*b 
5. a**b
''')
choose_option = int(input("Enter option: "))
while choose_option not in [1,2,3,4,5]:
    print ("Вы ввели неккореткное значение: ")
    choose_option = int(input("Enter option: "))

a = input("insert a: ")
b = input("insert b: ")
try:
    a = int(a)
    b = int(b)

except:
    print ("Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором")
    exit()

if choose_option == 1:
    c = sum_numbers(a, b)
if choose_option == 2:
    c = difference_numbers(a, b)
if choose_option == 3:
    c = division_numbers(a, b)
if choose_option == 4:
    c = multiplication_numbers(a, b)
if choose_option == 5:
    c = degree_numbers(a, b)


