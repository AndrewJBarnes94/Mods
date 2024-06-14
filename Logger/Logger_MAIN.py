from Logger import Logger

if __name__ == "__main__":
    # Create logger for CSV
    csv_logger = Logger("logfile.csv", "csv")
    csv_logger.log("This is an info message.")
    csv_logger.log("This is a warning message.", log_type='WARNING')
    csv_logger.log("This is an error message.", log_type='ERROR')

    # Create logger for TXT
    txt_logger = Logger("logfile.txt", "txt")
    txt_logger.log("This is an info message.")
    txt_logger.log("This is a warning message.", log_type='WARNING')
    txt_logger.log("This is an error message.", log_type='ERROR')
