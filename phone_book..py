

def main_menu():
    print('1 - открыть файл')
    print('2 - сохранить файл')
    print('3 - показать телефонную книгу')
    print('4 - добавить контакт')
    print('5 - найти контакт')
    print('6 - изменить контакт')
    print('7 - удалить контакт')
    print('8 - выход')
    print('9 - очистить телефонную книгу')
    while True:
        menu = int(input('Действие: '))

        if menu == 1:
            print(open_file())
        elif menu == 2:
            print()
        elif menu == 3:
            print(reading_file())
        elif menu == 4:
            print(add_people(), add_phones())
        elif menu == 5:
            print(find_contact())
        elif menu == 6:
            print()
        elif menu == 7:
            print()
        elif menu == 8:
            print()
        elif menu == 8:
            print(clear_all())

def change_contact():
    with open ('phone_book.txt', 'w', encoding='UTF-8') as contacts:
        contacts.write(input())

        

def clear_all():
    with open ('phone_book.txt', 'w+', encoding='UTF-8') as data:
        data.write ('')
    data.close()

def open_file():
    with open ('phone_book.txt', 'a', encoding='UTF-8') as data:
        data.read()
    data.close() 

def add_phones():
    with open ('phone_book.txt', 'a', encoding='UTF-8') as phones:# режим w перезаписывает и создает файл если его нет
        phones.write(input('Введите номер телефона: \n'))
        phones.close()
        # phones.write('89098105393\n') # \n делает перенос
        # phones.write('89144935677\n')

def add_people():
    people = open('phone_book.txt', 'a', encoding='UTF-8')
    surname = input('Введите фамилия: \n').capitalize()
    name = input('Введите имя: \n').capitalize() # исправляет текст и делает первую букву слова заглавной а остальные строчные
    middle_name = input('Введите отчество: \n').capitalize()
    people.write(f'{surname} {name} {middle_name}')
    people.close()

def reading_file():
    data = open('phone_book.txt', 'r', encoding='UTF-8')
    print(data.read())
    data.close()

def find_contact():
    with open ('phone_book.txt', 'r', encoding='UTF-8') as book:
        find = (input('Введите искомый параметр: \n'))
        list_contacts = []
        for line in book:
            list_contacts.append(line.strip()) # исключает пробелы
        print(list_contacts)
        for item in list_contacts:
            res = item.split()
            print(res)
            for i in range(len(res)): 
                if res[i] in find:
                    print(item)
        # book.close()    

main_menu()


# open_file()

# phones = open('phone_book.txt', 'r')# режим r читает файл
# for phone in phones:
#     print(phone)# вытащит все элементы из файла и запишет их в терминал
# phones.close() # завершает работу, закрывает файл

# with open ('phone_book.txt', 'w+') as people: