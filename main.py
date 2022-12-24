import os
import re
from datetime import datetime, timedelta
from AddressBook import AddressBook
from Record import Record
from messages import messages


book = AddressBook()


def hello(promt: str):
    return 'How can I help you?'

def add(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError('More arguments needed')
        case 1:
            raise ValueError('More arguments needed')
        case 2:
            rec = Record(arguments[0],[ arguments[1]])
            book.add_record(rec)
            return 'Done'
        case _:
            raise ValueError('Too many arguments')

def phone(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError('More arguments needed')
        case 1:
            try:
                res = ""
                for phone in book.find_user(arguments[0]).phones:
                    res += str(phone) + "\n"
                if res:
                    return res
                else:
                    raise ValueError('Phone not found')
            except:
                raise ValueError('Phone not found')
        case _:
            raise ValueError('messages.get(2)')

def finish(promt: str):
    return 'Good bye!'

def days_to_bd(promt: str):
    return book.find_user(promt).days_to_birthday()

def search(promt: str):
    return book.search(promt)

OPERATIONS = {
    'hello': hello,
    'add': add,
    'change': add,
    'phone': phone,
    'good bye': finish,
    'close': finish,
    'exit': finish,
    'fuck off': finish,
    'show birthdays in n days': days_to_bd,
    'search': search
}

def parse(promt: str):
    command = ''
    arguments = ''
    for operation in OPERATIONS.keys():
        if operation in promt.lower():
            command = str(operation)
            break
    if command != '':
        arguments = promt[len(command + ' '):]
        return OPERATIONS.get(command)(arguments)
    else:
        raise ValueError(messages.get(0))


def main():
    book.load_book()
    os.system('CLS')
    print(messages.get(-2))
    while True:
        command = input()
        res = parse(command)
        print(res)
        if res == messages.get(5):
            book.save_book()
            break
        

main()