

class TextFile_Handler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, data):
        with open(self.file_path, 'w') as file:
            file.write(data)

    def append_file(self, data):
        with open(self.file_path, 'a') as file:
            file.write(data)