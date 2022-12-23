import pickle
from Note import Note
from collections import UserDict

class NoteBook(UserDict):
    def add_note(self, note: Note):
        pass
    
    def find_note(self, promt: str):
        pass

    def load_book(self, filename: str = "Notes.not"): # Уже запилено
        try:
            with open(filename, "rb") as f:
                data = f.read()
                self.data = pickle.loads(data)
        except:
            print("Notebook not found")

    def save_book(self, filename: str = "Notes.not"): # Уже запилено
        try:
            with open(filename, "wb") as f:
                dump = pickle.dumps(self.data)
                f.write(dump)
        except:
            print("Notebook not saved")