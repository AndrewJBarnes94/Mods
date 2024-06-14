class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def open_file(self, mode='r'):
        try:
            self.file = open(self.file_path, mode)
            print(f"File {self.file_path} opened in {mode} mode.")
        except Exception as e:
            print(f"Error opening file: {e}")
            self.file = None

    def read_file(self):
        if self.file and not self.file.closed:
            try:
                content = self.file.read()
                return content
            except Exception as e:
                print(f"Error reading file: {e}")
                return None
        else:
            print("File is not open.")
            return None

    def write_file(self, content):
        if self.file and not self.file.closed and self.file.mode in ['w', 'a', 'r+']:
            try:
                self.file.write(content)
                print("Content written to file.")
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print("File is not open in write mode.")

    def close_file(self):
        if self.file and not self.file.closed:
            try:
                self.file.close()
                print(f"File {self.file_path} closed.")
            except Exception as e:
                print(f"Error closing file: {e}")
