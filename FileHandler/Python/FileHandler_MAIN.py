from FileHandler import FileHandler

# Writing to the file
file_handler = FileHandler("example.txt")
file_handler.open_file('w')
file_handler.write_file("Hello, World!")
file_handler.close_file()

# Reading from the file
file_handler.open_file('r')
content = file_handler.read_file()
print(content)
file_handler.close_file()
