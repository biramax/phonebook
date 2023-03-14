def greetings():
    print('Здравствуйте, уважаемый пользователь!')

def menu():
    print('Введите 1, если хотите ввести данные нового абонента')
    command = int(input('Ведите вашу команду: '))
    return int(input('Ведите вашу команду: '))
def show_contact_form():
    family = print('Введите фамилию: ')
    name = print('Введите имя: ')
    phone = print('Введите номер телефона: ')
    return {'family': family, 'name': name, 'phone': phone}

def show_phonebook(date):
    return None