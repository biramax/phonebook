def read_phonebook():
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        return file.read()


def add_contact(cont):
    data = open('file_name.txt', 'a')
    data.write(cont['family']+' '+cont['name']+' '+cont['phone']+'\n')

def find(text):
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        res_list = []
        for line in file:
            if text in line:
                res_list.append(line)
        return res_list
    


# print(read_phonebook())
# data = {'family': 'QweSDArty', 'name': 'ytreDfFDwq', 'phone':'phone'}
# add_contact(data)
# data1 = data['name'], data['surname']
# print(data1)
# print(find('Cccc'))