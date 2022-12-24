from collections import UserDict
import Record
import pickle

class AddressBook(UserDict):
    def load_book(self, filename: str = "data.ph")->bool: # Уже запилено
        try:
            with open(filename, "rb") as f:
                data = f.read()
                self.data = pickle.loads(data)
                return True
        except:
            return False

    def save_book(self, filename: str = "data.ph")->bool: # Уже запилено
        try:
            with open(filename, "wb") as f:
                dump = pickle.dumps(self.data)
                f.write(dump)
                return True
        except:
            return False
    
    def add_record(self, record: Record):
        pass

    def update_record(self, record: Record):
        pass

    def find_user(self, name: str) -> Record:
        pass

    def search(self, promt):
        pass
    
    def add_phone(self, user: str, phone: str): # пхоня передается в формате 380999279480. Формат хранения либо оставить такой, либо обсудить
        pass
    
    def add_address(self, user: str, address: str):
        pass

    def add_email(self, user: str, email: str):
        pass

    def add_birthday(self, user: str, birthday: str):
        pass

    def find_users_by_days_to_bd(self, count: int):
        pass