phon_book = []

def open_phon_book():
    with open('phon_book_txt', 'r', encoding = 'utf-8') as data:
        phon_book = data.readlines()
        print('Файл открыт')
        return phon_book

def save_phon_book():
    with open('phon_book_txt', 'w', encoding = 'utf-8') as data:
        for i in phon_book:
            data.write(i)

def show_phon_book(file):
    print(phon_book)
    if len(phon_book) == 0:
        print('Вы не открыли файл, либо файл пуст!')
    else:
        for i in phon_book:
            print(' '.join(i.split(';')))

def add_phon_book():
    if len(phon_book) == 0:
        print('Вы не открыли файл, либо файл пуст!')
    else:
        user_info = input('Введите контакты нового пользователя: ')
        user_info = ';'.join(user_info.split(' '))
        phon_book.append(user_info + '\n')

def change_phon_boor():
    user_info = input('Введите номер контакта для изменения: ')
    for i in range(len(phon_book)):
        if user_info in phon_book[i]:
            print(phon_book[i])
            new_user_info = input('Введите новые данные контакта: ')
            phon_book[i] = phon_book[i].replace(user_info, new_user_info)

def search_phon_book():
    user_info = input('Введите данные контакта, по которым вы хотите найи контак.')
    for i in range(len(phon_book)):
        if user_info in phon_book[i]:
            print(phon_book[i])

def delete_hphon_book():
    user_info = input('Введите данные контакта, который вы хотите удалить.')
    for i in range(len(phon_book)):
        if user_info in phon_book[i]:
            print(phon_book[i])
            phon_book.pop(i)