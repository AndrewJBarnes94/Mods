from datetime import datetime
from FileHandler import FileHandler

class Logger:
    def __init__(self, filename, file_format='txt'):
        self.file_handler = FileHandler(filename, file_format)
        self.file_handler.open_file('a')

    def log(self, message, log_type='INFO'):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.file_handler.write_log(timestamp, log_type, message)
