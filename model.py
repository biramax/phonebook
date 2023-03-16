def read_phonebook():# Вывод телефоной книги
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        return file.read()


def add_contact(cont):# Добавление контакта
    data = open('file_name.txt', 'a', encoding='utf-8')
    data.write(cont['family']+' '+cont['name']+' '+cont['phone']+'\n')

def find(text): # Поиск контакта по ключевому слову
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        res_list = []
        for line in file:
            if text in line:
                res_list.append(line)
        return res_list


def find_first(text): # Находит по запросу первый контакт
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        res_list = []
        for line in file:
            if text in line:
                return line
        return res_list


def find_and_change(old_text, new_text): # Удаление старый и добавление новых
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if old_text in line:
                with open("file_name.txt", "r") as file:
                    lines = file.readlines()
                del lines[count]
                
                with open("file_name.txt", "w") as file:
                    file.writelines(lines)
                data = open('file_name.txt', 'a', encoding='utf-8')
                data.write(new_text['family']+' '+new_text['name']+' '+new_text['phone']+'\n')
                break
            else:
                count += 1


    
def find_and_del_firs(text): # Удаляет первый найденный контакт
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if text in line:
                with open("file_name.txt", "r") as file:
                    lines = file.readlines()
                del lines[count]
                
                with open("file_name.txt", "w") as file:
                    file.writelines(lines)
                return True
            else:
                count += 1
        
        return False
    