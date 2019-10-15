from app import library_app

if __name__ == '__main__':
    """
    The main method of the program
    """
    # The list of books to read in and save
    book_info_list1 = open("Step1Data.txt").readlines()
    book_info_list2 = open("Step2Data.txt").readlines()
    book_info_list3 = open("Step3Data.txt").readlines()
    library_app.parse_document_list(book_info_list1)  # Parse the file and add each book to the dictionary
    library_app.parse_document_list(book_info_list2)  # Parse the file and add each book to the dictionary
    library_app.parse_document_list(book_info_list3)  # Parse the file and add each book to the dictionary

    isRunning = True  # Sets flag in order to be able to break out of the loop
    while isRunning:
        key = input("Which document would you like to access? (Or type END to exit the program): ").lower()
        if key.lower() == "end":  # ends program is user chooses to do so
            isRunning = not isRunning
        else:
            library_app.parse_user_input(key)  # parses key user inputs
