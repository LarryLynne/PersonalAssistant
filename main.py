import os
import re
from datetime import datetime, timedelta
from AddressBook import AddressBook
from Record import Record
from messages import messages


def error_processor(func):
    def inner(promt: str):
        try:
            return func(promt)
        except ValueError as exception:
            return exception.args[0]
        except StopIteration as exception:
            pass
        except KeyError as exception:
            return exception.args[0]
    return inner


def hello(promt: str):
    return 'How can I help you?'

@error_processor
def add(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError(messages.get(1))
        case 1:
            raise ValueError(messages.get(1))
        case 2:
            rec = Record(arguments[0], [arguments[1]])
            book.add_record(rec)
            return messages.get(-1)
        case 3:
            rec = Record(arguments[0], [arguments[1]], arguments[2])
            book.add_record(rec)
            return messages.get(-1)
        case _:
            raise ValueError(messages.get(2))

@error_processor
def phone(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError(messages.get(1))
        case 1:
            try:
                res = ""
                for phone in book.find_user(arguments[0]).phones:
                    res += str(phone) + "\n"
                if res:
                    return res
                else:
                    raise ValueError(messages.get(4))
            except:
                raise ValueError(messages.get(4))
        case _:
            raise ValueError(messages.get(2))

@error_processor
def finish(promt: str):
    return messages.get(5)

@error_processor
def add_phone(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError(messages.get(1))
        case 1:
            raise ValueError(messages.get(1))
        case 2:
            book.add_phone(arguments[0], arguments[1])
            return messages.get(-1)
        case _:
            raise ValueError(messages.get(2))


@error_processor
def add_address(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError(messages.get(1))
        case 1:
            raise ValueError(messages.get(1))
        case 2:
            book.add_address(arguments[0], arguments[1])
            return messages.get(-1)
        case _:
            raise ValueError(messages.get(2))

@error_processor
def add_email(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError(messages.get(1))
        case 1:
            raise ValueError(messages.get(1))
        case 2:
            book.add_email(arguments[0], arguments[1])
            return messages.get(-1)
        case _:
            raise ValueError(messages.get(2))

@error_processor
def add_birthday(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError(messages.get(1))
        case 1:
            raise ValueError(messages.get(1))
        case 2:
            book.add_birthday(arguments[0], arguments[1])
            return messages.get(-1)
        case _:
            raise ValueError(messages.get(2))

@error_processor
def days_to_bd(promt: str):
    res = []
    usr: Record
    try:
        n = int(promt)
        users = list(book.data.keys())
        for user in users:
            usr = book.find_user(str(user))
            if usr.days_to_birthday() == n:
                res.append(str(usr))
    except:
        raise ValueError(messages.get(15))
    return res

@error_processor
def search(promt: str):
    return book.search(promt)

OPERATIONS = {
    'hello': hello, # +
    'add user': add, # +
    'change': add,
    'find phone': phone, # +
    'good bye': finish, # +
    'close': finish, # +
    'exit': finish, # +
    'fuck off': finish, # +
    'show birthdays in n days': days_to_bd, # +
    'search': search,
    'add address': add_address,
    'add email': add_email,
    'add birthday': add_birthday,
    'add phone': add_phone # +
}

@error_processor
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

book = AddressBook()

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