def read_phonebook():
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        pass

    return None

def add_contact(data):
    surname = input("Введите фамилию")
    name = input("Введите имя")
    phonebook = input("Введите номер телефона")
    data = open('file_name.txt', 'a')
    data.writelines(surname)

def find():
    a = 'cool text'
    print ('text' in a) 
    return None
