#pragma once  // Ensure this header is included only once
#include <string>
#include <fstream>

// Class for basic file operations
class FileHandler {
public:
    // Default constructor
    FileHandler() = default;

    // Default destructor
    ~FileHandler() = default;

    // Create a file at the given path
    void createFile(const std::string& filePath);

    // Write content to a file at the given path
    void writeFile(const std::string& filePath, const std::string& content);

    // Read content from a file at the given path
    std::string readFile(const std::string& filePath);
};
