#include "FileHandler.h"  // Include the header file
#include <stdexcept>      // For runtime_error exceptions
#include <sstream>        // For string streams

// Create a file at the specified path
void FileHandler::createFile(const std::string& filePath) {
    std::ofstream file(filePath);  // Open file stream for writing
    if (!file) {  // Check if the file was created successfully
        throw std::runtime_error("Unable to create file: " + filePath);  // Throw error if not
    }
    file.close();  // Close the file
}

// Write content to a file at the specified path
void FileHandler::writeFile(const std::string& filePath, const std::string& content) {
    std::ofstream file(filePath);  // Open file stream for writing
    if (!file) {  // Check if the file was opened successfully
        throw std::runtime_error("Unable to open file: " + filePath);  // Throw error if not
    }
    file << content;  // Write content to the file
    file.close();  // Close the file
}

// Read content from a file at the specified path
std::string FileHandler::readFile(const std::string& filePath) {
    std::ifstream file(filePath);  // Open file stream for reading
    if (!file) {  // Check if the file was opened successfully
        throw std::runtime_error("Unable to open file: " + filePath);  // Throw error if not
    }
    std::ostringstream ss;
    ss << file.rdbuf();  // Read the file content into the string stream
    return ss.str();  // Return the file content as a string
}
