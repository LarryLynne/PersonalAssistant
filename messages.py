from colorama import Fore
messages = {
    -2: Fore.CYAN + "- Hello! Let's get started!" + Fore.RESET,
    -1: Fore.GREEN + '- Done' + Fore.RESET,
    0: Fore.RED + '- Unknown command' + Fore.RESET,
    1: Fore.RED + '- More arguments needed' + Fore.RESET,
    2: Fore.RED + '- Too many arguments' + Fore.RESET,
    3: Fore.RED + '- Incorrect phone' + Fore.RESET,
    4: Fore.RED + '- Phone not found' + Fore.RESET,
    5: Fore.MAGENTA + '- Good bye!' + Fore.RESET,
    6: Fore.CYAN + '- How can I help you?' + Fore.RESET,
    7: Fore.RED + '- There is no any records in phonebook' + Fore.RESET,
    8: Fore.RED + '- Incorrect phone number' + Fore.RESET,
    9: Fore.RED + '- Invalid date of birth' + Fore.RESET,
    10: Fore.RED + '- User already exists' + Fore.RESET,
    11: Fore.RED + '- User not found' + Fore.RESET,
    12: Fore.RED + '- Address book not saved' + Fore.RESET,
    13: Fore.RED + '- Cannot load address book' + Fore.RESET,
    14: Fore.RED + '- Users not found' + Fore.RESET,
    15: '- Notebook not found',
    16: '- Notebook not saved',
    17: '- There is no tags',
    18: '- There is no notes with tag ',
    19: '- Search tag must start with # and contain at least 1 character ',
    20: '- There is no notes with text ',
    21: '- There is no note '
    22: Fore.RED + '- Bad number of days' + Fore.RESET
}