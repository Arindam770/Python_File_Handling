import json

class Json_Handler:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_json_dict(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data


    def write_json_dict(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

if __name__ == '__main__':
    json_handler = Json_Handler('Sample_Files\\DummyData.json')
    data = json_handler.read_json_dict()
    print(data) 
    json_handler.write_json_dict(data)