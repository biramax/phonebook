def read_phonebook():
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        return file.read()


def add_contact(cont):
    data = open('file_name.txt', 'a', encoding='utf-8')
    data.write(cont['family']+' '+cont['name']+' '+cont['phone']+'\n')

def find(text):
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        res_list = []
        for line in file:
            if text in line:
                res_list.append(line)
        return res_list
    
def find_and_del_firs(text):
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
    



# print(read_phonebook())
# data = {'family': 'аеарывпывае', 'name': 'ыпвппвп', 'phone':'ыкппвкпывк'}
# add_contact(data)
# data1 = data['name'], data['surname']
# print(data1)
# print(find('Cccc'))
# print(find_and_del_firs('вапрарвар'))
# with open("file_name.txt", "r") as file:
#     lines = file.readlines()
# del lines[0]
# with open("file_name.txt", "w") as file:
#     file.writelines(lines)