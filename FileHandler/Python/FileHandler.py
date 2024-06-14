import csv
from datetime import datetime
from Logger import Logger

class FileHandler:
    def __init__(self, file_path, file_format='txt'):
        self.file_path = file_path
        self.file_format = file_format.lower()
        self.file = None
        self.logger = Logger("file_handler_log.csv", "csv")
        if self.file_format == 'csv':
            self.initialize_csv_file()

    def initialize_csv_file(self):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Log Type', 'Message'])

    def open_file(self, mode='r'):
        try:
            self.file = open(self.file_path, mode, newline='' if self.file_format == 'csv' else None)
            self.logger.log(f"File {self.file_path} opened in {mode} mode.", "INFO")
        except Exception as e:
            self.logger.log(f"Error opening file: {e}", "ERROR")
            self.file = None

    def read_file(self):
        if self.file and not self.file.closed:
            try:
                content = self.file.read()
                return content
            except Exception as e:
                self.logger.log(f"Error reading file: {e}", "ERROR")
                return None
        else:
            self.logger.log("File is not open.", "WARNING")
            return None

    def write_file(self, content):
        if self.file and not self.file.closed and self.file.mode in ['w', 'a', 'r+']:
            try:
                if self.file_format == 'csv':
                    writer = csv.writer(self.file)
                    writer.writerow(content)
                else:
                    self.file.write(content)
                self.logger.log("Content written to file.", "INFO")
            except Exception as e:
                self.logger.log(f"Error writing to file: {e}", "ERROR")
        else:
            self.logger.log("File is not open in write mode.", "WARNING")

    def close_file(self):
        if self.file and not self.file.closed:
            try:
                self.file.close()
                self.logger.log(f"File {self.file_path} closed.", "INFO")
            except Exception as e:
                self.logger.log(f"Error closing file: {e}", "ERROR")

    def write_log(self, timestamp, log_type, message):
        if self.file_format == 'csv':
            self.write_file([timestamp, log_type, message])
        else:
            log_entry = f"{timestamp} - {log_type}: {message}\n"
            self.write_file(log_entry)
