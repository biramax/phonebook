import model
import view

def run():
    view.greetings()

    while True:
        
        command = view.menu()

        # Добавление нового пользователя:
        # view предлагает пользователю заполнить в отдельных полях фамилию, имя и телефон и возвращает словарь {'family': фамилия, 'name': имя, 'phone': телефон}
        # в model передаётся этот словарь, записывается новая строка в файл phonebook.txt: фамилия,имя,телефон
        if command == 1:
            data = view.show_contact_form()
            model.add_contact(data)

            # во view нужно создать ф-ю show_message()
            view.show_message('Контакт успешно добавлен')

        # Считывание данных из телефонной книги:
        # model возвращает список: 
        # [
        #   "фамилия, имя, телефон",
        #   "фамилия, имя, телефон",
        #   "фамилия, имя, телефон",
        #   ...
        # ]
        # view этот список пропускает через цикл и выдаёт в консоль
        if command == 2:
            data = model.read_phonebook()
            view.show_phonebook(data)

        # Поиск:
        # view запрашивает у пользователя поисковую фразу и возвращает в виде строки
        # model производит поиск подстроки по каждой строке файла и возвращает список, как в предыдущем пункте.
        # во view для вывода списка мы воспользуемся функцией из предыдущего пункта show_phonebook
        if command == 3:
            search = view.get_search_query()
            data = model.find(search)
            if len(data) == 0:
                view.show_message('Пользователь не найден')
            else:
                view.show_phonebook(data)

        # Изменение данных:
        # во view изспользуем функцию из предыдущего пункта get_search_query, возвращается строка с поисковой фразой
        # model производит поиск подстроки, как в предыдущем пункте, но возвращает не всех найденных, а только первого (нужно создать ф-ю find_first), возврат стандартно в виде списка, хотя и из всего одного элемента: 
        # [
        #   "фамилия, имя, телефон",
        # ]
        # во view для вывода списка мы воспользуемся ф-й show_phonebook, и для сбора новых данных ф-й show_contact_form()
        # model создаёт ф-ю find_and_change, в которую передаётся: 
        #   - search, это та же строка поиска, что и раньше, чтобы снова можно было найти первого подходящего пользователя, чтобы заменить его на новые данные
        #   - data - новые данные пользователя
        if command == 4:
            view.show_message('Введите поисковую фразу')
            search = view.get_search_query()
            data = model.find_first(search)
            if len(data) == 0:
                view.show_message('Пользователь не найден')    
            else: 
                view.show_phonebook(data)
                view.show_message('Введите новые данные пользователя')
                data = view.show_contact_form()
                model.find_and_change(search, data)
                view.show_message('Данные успешно изменены')

        # Удаление данных:
        # во view изспользуем функцию из предыдущего пункта get_search_query, возвращается строка с поисковой фразой
        # model производит поиск подстроки, и удаляет первого подходящего пользователя, возвращает True, если пользователь найден, False - если не найден
        if command == 5:
            view.show_message('Введите поисковую фразу')
            search = view.get_search_query()
            found = model.find_and_del_first(search)
            if found == False:
                view.show_message('Пользователь не найден')
            else:
                view.show_message('Пользователь успешно удалён')

        if command == 6:
            break