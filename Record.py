class Record:
    def __init__(self, user_name: str, user_phones: tuple = (), user_birthday: str = '') -> None:
        pass

    def __str__(self) -> str: # Надо для поиска
        pass
    
    def add_phone(self, user_phone: str):
        self.phones.append(Phone(user_phone))
    
    def add_address(self, user_address: str):
        pass

    def add_email(self, user_email: str):
        self.emails.append(Phone(user_email))

    def add_birthday(self, user_birthday: str):
        pass

    def days_to_birthday(self):
        pass
    
