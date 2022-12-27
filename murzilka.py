commands = {
    'hello': '[     ]',
    'add user': '[user][phone][*birthday]',
    'find phone': '[user name]',
    'find user': '[user name]',
    'good bye': '[     ]',
    'close': '[     ]',
    'exit': '[     ]',
    'show birthdays in n days': '[number of days to BD]',
    'search': '[any text]',
    'add address': '[user name][address]',
    'add email': '[user name][email]',
    'add birthday': '[user name][birthday]',
    'add phone': '[user name][phone]',
    'delete user': '[user name]',
    'delete contact': '[user name]',
    'write note': '[some text where the first word is a caption, and some other words with # in a beginnig are hashtags]',
    'find note': '[promt]',
    'delete note': '[note caption]',
    'show all tags': '[     ]',
    'get all notes': '[     ]',
    'update note': '[note caption][text]',
    'find notes tags': '[*tag]',
}



for c in commands:
    #print((c + '{:<20}'.commands.get(c)))
    print("{:<30}{:<30}".format(c, commands.get(c)))  # |left      |**center**|     right|
