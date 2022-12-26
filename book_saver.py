import os
import pickle
from messages import messages


class BookSaver:
    def load_book(self, filename: str):
        file_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents', filename)
        try:
            with open(file_path, "rb") as f:
                data = f.read()
                self.data = pickle.loads(data)
        except:
            print(messages.get(13).format('filename', filename))  # 13: '- Cannot load file {filename}'

    def save_book(self, filename: str):
        try:
            file_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents', filename)
            with open(file_path, "wb") as f:
                dump = pickle.dumps(self.data)
                f.write(dump)
        except:
            print(messages.get(12) + ' ' + filename)  # 12:'- File {filename} not saved',
