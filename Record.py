from datetime import datetime, timedelta
from Phone import Phone
from Name import Name
from BirthDay import BirthDay
from Email import Email
from Address import Address

class Record:
    def __init__(self, user_name: str, user_phones: tuple = (), user_birthday: str = '') -> None:
        self.name: Name = Name(user_name)
        self.phones: list[Phone] = list()
        for uph in user_phones:
            self.add_phone(uph)

        self.birthday: BirthDay = BirthDay(user_birthday)
        self.address: str
        self.emails: list[Email] = list()

    def __str__(self) -> str:
        res = str(self.name) + ", phones: "
        for ph in self.phones:
            res += str(ph) + ", "
        res += "birthday: " + str(self.birthday) + ", "
        for em in self.emails:
            res += str(em) + ", "
        res += "address: " + self.address

        return res

    def add_phone(self, user_phone: str):
        self.phones.append(Phone(user_phone))

    def days_to_birthday(self)-> int:
        if self.birthday:
            today = datetime.now().date()
            db = datetime(year=datetime.now().year, month=int(str(self.birthday).split("-")[1]),
                          day=int(str(self.birthday).split("-")[2]))
            db = db.date()
            if db < today:
                db += timedelta(days=365)
            return (db - today).days
        else:
            return -1

    def add_address(self, user_address: str):
       self.address = Address(user_address)

    def add_email(self, user_email: str):
        self.emails.append(Phone(user_email))

    def add_birthday(self, user_birthday: str):
        self.birthday = BirthDay(user_birthday)
