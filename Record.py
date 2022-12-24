from datetime import datetime, timedelta

class Record:
    def __init__(self, user_name: str, user_phones: tuple = (), user_birthday: str = '') -> None:
        self.name: Name = Name(user_name)
        self.phones: list[Phone] = list()
        for uph in user_phones:
            self.add_phone(uph)

        self.birthday: BirthDay = BirthDay(user_birthday)

    def __str__(self) -> str:
        res = str(self.name) + ", phones: "
        for ph in self.phones:
            res += str(ph) + ", "
        res += "birthday: " + str(self.birthday)
        return res

    def add_phone(self, user_phone: str):
        self.phones.append(Phone(user_phone))

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            db = datetime(year=datetime.now().year, month=int(str(self.birthday).split("-")[1]),
                          day=int(str(self.birthday).split("-")[2]))
            db = db.date()
            if db < today:
                db += timedelta(days=365)
            return (db - today).days
        else:
            return 'ХЗ'

    def add_address(self, user_address: str):
        pass

    def add_email(self, user_email: str):
        pass

    def add_birthday(self, user_birthday: str):
        pass
