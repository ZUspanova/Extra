users = []

option = input(
    'Choose one option:\n1. Create user\n2. Show list of users\n3. Delete user from list\n4. Authorization\n5. Exit')

# статус входа в аккаунт
logged_in = False

while option != '5':
    # добавить юзера
    if option == '1':
        user = {}
        user['Name'] = input('Name:')
        user['Surname'] = input('Surname:')
        user['Age'] = input('Age:')

        user['Address'] = input('Address:')

        # проверить есть ли юзер в списке и если там вообще юзеры
        email = input('Email:')
        email_exists = False
        while True and len(users) != 0:
            for i in users:
                if email in i['Email']:
                    email_exists = True
            if email_exists:
                email = input('Email already exists, enter another:')
                email_exists = False
            else:
                break

        user['Email'] = email

        # проверить количество символов в пароле
        password = input('Password:')
        while not len(password) > 7:
            password = input('Password should be longer\nPassword:')
        user['Password'] = password

        users.append(user)

    # вывести список юзеров
    elif option == '2':
        if len(users) == 0:
            print('There are no users in the list')
        else:
            for i in users:
                cur = ''
                for j in i:
                    # выводим все данные юзера в одну строку
                    cur += f"{j}: {i[j]}, "
                print(cur)

    # удалить юзера
    elif option == '3':
        name = input('Name:')
        for i in range(len(users)):
            if users[i]['Name'] == name:
                del users[i]

    # авторизция
    elif option == '4':
        # если не злогинились, заходим
        if not logged_in:
            email = input('Authorization\nEnter email:')
            user_exists = False
            i = 0
            for i in range(len(users)):
                if users[i]['Email'] == email:
                    user_exists = True
                    num = i
                i += 1

            # заходим в акк если найден имейл юзера
            if user_exists:
                correct_password = users[num]['Password']
                password = input('Password:')
                while password != correct_password:
                    password = input('Wrong password\nEnter password:')
                print('You are succesfully logged in to the system')
                print(f"Hello, {users[num]['Name']}")
                logged_in = True
            else:
                # юзер не найден
                print('User does not exist')
        else:
            # выходим из акка если уже залогинились
            print('You are succesfully logged out')
            logged_in = False

    if not logged_in:
        option = input(
            '\nChoose one option:\n1. Create user\n2. Show list of users\n3. Delete user from list\n4. Authorization\n5. Exit')
    else:
        option = input(
            '\nChoose one option:\n1. Create user\n2. Show list of users\n3. Delete user from list\n4. Log out\n5. Exit')

print('Good Bye')
