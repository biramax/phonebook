def read_phonebook():
    # with open('file_name.txt', 'r', encoding='utf-8') as file:
    #     pass
    myfile = open("file_name.txt", "r")
    return myfile.read()

def add_contact(cont):
    data = open('file_name.txt', 'a')
    data.writelines(cont['family'])
    data.writelines(' ')
    data.writelines(cont['name'])
    data.writelines(' ')
    data.writelines(cont['phone'])
    data.writelines('\n')

def find(text):
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        resultat = []


# print(read_phonebook())
# data = {'family': 'Qwerty', 'name': 'ytrewq', 'phone':'phone'}
# add_contact(data)
# data1 = data['name'], data['surname']
# print(data1)