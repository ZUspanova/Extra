
print ("Здравствуйте, вы проходите анкету")

name = input ("Введите ваше имя: ")
username = input ("Введите вашу фамилию: ")
age = input ("Введите ваш год рождения: ")
year_of_birth = input("Нравится ли вам курс?: ")
purpose_lesson = input ("Что вы ожидаете в дальнейших занятиях?: ")

print ("Вы заполнили такие данные: ")
print ("Вас зовут", name, username)
print ("Вам", int(age) - 2023, "лет")
print ("Ваш ответ к первому вопросу: ", year_of_birth)
print ("Ваш ответ к второму вопросу: ", purpose_lesson)