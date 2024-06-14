#include <iostream>  // For standard input/output
#include "FileHandler.h"  // Include the FileHandler class

int main() {
    FileHandler fileHandler;  // Create an instance of FileHandler

    std::string filePath = "example.txt";  // Define the file path
    std::string content = "Hello, this is a test file.";  // Define the content to write

    try {
        fileHandler.createFile(filePath);  // Create a new file
        std::cout << "File created successfully." << std::endl;

        fileHandler.writeFile(filePath, content);  // Write content to the file
        std::cout << "Content written to file successfully." << std::endl;

        std::string fileContent = fileHandler.readFile(filePath);  // Read content from the file
        std::cout << "Content read from file: " << fileContent << std::endl;
    } catch (const std::exception& ex) {
        std::cerr << "Error: " << ex.what() << std::endl;  // Handle any errors
    }

    return 0;  // End of the program
}
