import os
import re
from datetime import datetime, timedelta
from AddressBook import AddressBook
from Record import Record
from messages import messages
from Note import Note
from NoteBook import NoteBook

book = AddressBook()
notes = NoteBook()

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
    return messages.get(6)

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
        raise ValueError(messages.get(22))
    return res

@error_processor
def search(promt: str):
    return book.search(promt)

@error_processor
def delete_contact(promt: str):
    arguments = promt.split(" ")
    l = len(arguments)
    match l:
        case 0:
            raise ValueError(messages.get(1))
        case 1:
            book.delete_contact(arguments[0])
            return messages.get(-1)
        case _:
            raise ValueError(messages.get(2))

@error_processor
def write_note(promt: str):
    note = Note(promt)
    notes.add_note(note)
    return messages.get(-1)


@error_processor
def find_note(promt: str):
    return notes.find_note(promt)

@error_processor
def del_note(promt: str):
    notes.del_note(promt)

@error_processor
def show_all_tags(promt: str):
    return notes.show_all_tags()

@error_processor
def get_all_notes(promt: str):
    return notes.get_all_notes()



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
    'search': search, # +
    'add address': add_address, # +
    'add email': add_email, # +
    'add birthday': add_birthday, # +
    'add phone': add_phone, # +
    'delete user': delete_contact, # +
    'delete contact': delete_contact, # +
    'write note': write_note,
    'find note': find_note,
    'delete note': del_note,
    'show all tags': show_all_tags,
    'get all notes': get_all_notes,
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
        possible_commands = guess_command(promt)
        if possible_commands:
            print(messages.get(24))
            i = 0
            for c in possible_commands:
                print(str(i) + ' - ' + c)
                i+=1
            new_command_key = int(input(messages.get(25)))
            if new_command_key<len(possible_commands):
                command = str(possible_commands[new_command_key])
                arguments = str(input(messages.get(26)))
                return OPERATIONS.get(command)(arguments)
            else:
                raise ValueError(messages.get(0))
        else:
            raise ValueError(messages.get(0))
        
        #raise ValueError(messages.get(0))


def guess_command(promt: str)-> list:
    #res = 0
    commands = list(OPERATIONS.keys())
    weight = 0.0
    possible_command = ''
    poss_cmds = []
    for c in commands:
        words = c.split(' ')
        cnt = len(promt.split(' '))
        cnt1 = len(promt)
        ii = 0
        i = 0
        for word in words:
            if word in promt:
                ii+=len(word)
                i+=1
        if (i/cnt)*(ii/cnt1) > weight:
            weight = (i/cnt)*(ii/cnt1)
            possible_command = c
            poss_cmds.insert(0, possible_command)
    #res = OPERATIONS.get(possible_command)
    return list(poss_cmds)


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
            notes.save_book()
            break

main()