
def import_data(file_to_add, phonebook):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{file_to_add} не найден')


def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения (дд.мм.гггг)', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по отчеству\n4 - по дате рождения\n5 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите отчество для поиска: ')
        print()
    elif search_field == '4':
        search_value = input('Введите дату рождения для поиска: ')
        print()
    elif search_field == '5':
        search_value = input('Введите номер телефона для поиска: ')
        print()
    return search_field, search_value


def find_contact(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Отчество', '4': 'Дата рождения', '5': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    second_name = input('Введите отчество: ')
    date_of_birth = input('Введите дату рождения (дд.мм.гггг): ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, second_name, date_of_birth, phone_number


def add_new_contact(file_name):
    info = ' '.join(get_new_contact())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите порядковый номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_contact(file_name):
    contact_list = read_file_to_list(file_name)
    contact_to_change = search_to_modify(contact_list)
    contact_list.remove(contact_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Дата рождения (дд.мм.гггг.)\n5 - Номер телефона\n')
    if field == '1':
        contact_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        contact_to_change[1] = input('Введите имя: ')
    elif field == '3':
        contact_to_change[2] = input('Введите отчество: ')
    elif field == '4':
        contact_to_change[3] = input('Введите дату рождения: ')
    elif field == '5':
        contact_to_change[4] = input('Введите номер телефона: ')
    contact_list.append(contact_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    contact_to_change = search_to_modify(contact_list)
    contact_list.remove(contact_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    print()

def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:18}', end='')
        print()