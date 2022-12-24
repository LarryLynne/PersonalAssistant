import pickle
from Note import Note
from collections import UserDict


class NoteBook(UserDict):
    def __init__(self):
        super().__init__()
        self.load_book()

    def __del__(self):
        self.save_book()

    def get_all_notes(self):
        result = ''
        keys = self.keys()
        for note in keys:
            result += str(self.get(note)) + '\n'
        return result

    def add_note(self, note: Note):
        self.update({str(note.caption): note})

    def del_note(self, promt: str):
        try:
            del self[promt]
        except:
            raise KeyError(f"There is no note '{promt}'")

    def update_note(self, note: Note):
        if self.get(str(note.caption)):
            self.update({str(note.caption): note})
        else:
            raise KeyError(f"There is no notes '{note.caption}'")

    def find_note(self, promt: str):
        result = ''
        keys = self.keys()
        for note in keys:
            if str(self.get(note)).find(promt) >= 0:
                result += str(self.get(note)) + '\n'
        if result:
            return result
        raise ValueError(f"There is no notes with text '{promt}'")

    def load_book(self, filename: str = "Notes.not"):
        try:
            with open(filename, "rb") as f:
                data = f.read()
                self.data = pickle.loads(data)
        except:
            print("Notebook not found")

    def save_book(self, filename: str = "Notes.not"):
        try:
            with open(filename, "wb") as f:
                dump = pickle.dumps(self.data)
                f.write(dump)
        except:
            print("Notebook not saved")
