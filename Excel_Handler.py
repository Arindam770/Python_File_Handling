import openpyxl

class Excel_Handler:

    def __init__(self, file_path):
        self.file_path = file_path

    def write_excel_dict(self, data):
        all_columns = data[0].keys()