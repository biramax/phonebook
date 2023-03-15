def read_phonebook():
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        pass

    return None

def add_contact(cont):
    data = open('file_name.txt', 'a')
    print(cont)
    data.writelines(cont['family'])
    data.writelines(' ')
    data.writelines(cont['name'])
    data.writelines(' ')
    data.writelines(cont['phone'])
    data.writelines('\n')

def find():
    a = 'cool text'
    print ('text' in a) 
    return None



# data = {'family': 'Qwerty', 'name': 'ytrewq', 'phone':'phone'}
# add_contact(data)
# # data1 = data['name'], data['surname']
# # print(data1)