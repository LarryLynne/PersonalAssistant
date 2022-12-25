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
        if self.data.get(str(record.name)):
            raise KeyError(f"User {record.name} already exists")
        else:
            self.data.update({str(record.name): record})
            #self.update({str(record.name): record})

    def update_record(self, record: Record):
        if self.get(str(record.name)):
           self.update({str(record.name): record})
        else:
             raise KeyError(f"User {record.name} not found")
   
    def find_user(self, name: str) -> Record:
        res = self.data.get(name)
        if res:
            return res
        else:
            raise KeyError(f"User {name} not found")

    def search(self, promt):
        pass
    
    def add_phone(self, user: str, phone: str): # пхоня передается в формате 380999279480. Формат хранения либо оставить такой, либо обсудить
        usr = self.find_user(user)
        if usr:
            usr.add_phone(phone)
        else:
            raise KeyError(f"User {user} not found")
    
    def add_address(self, user: str, address: str):
        pass

    def add_email(self, user: str, email: str):
        usr = self.find_user(user)
        if usr:
            usr.add_email(email)
        else:
            raise KeyError(f"User {user} not found")

    def add_birthday(self, user: str, birthday: str):
        pass

    def find_users_by_days_to_bd(self, count: int):
        pass