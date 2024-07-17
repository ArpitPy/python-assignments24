class LibraryBook:
    def __init__(self, book_name, author):
        self.__book_name = book_name  # Encapsulated attribute for book name
        self.__author = author        # Encapsulated attribute for author
        self.__available = True       # Encapsulated attribute for availability status
    
    # Getter methods
    def get_book_name(self):
        return self.__book_name
    
    def get_author(self):
        return self.__author
    
    def is_available(self):
        return self.__available
    
    # Method to borrow a book
    def borrow_book(self):
        if self.__available:
            self.__available = False
            print(f"Book '{self.__book_name}' by {self.__author} has been borrowed.")
        else:
            print(f"Sorry, '{self.__book_name}' is currently not available.")
    
    # Method to return a book
    def return_book(self):
        if not self.__available:
            self.__available = True
            print(f"Book '{self.__book_name}' by {self.__author} has been returned.")
        else:
            print(f"Error: '{self.__book_name}' is already available.")
    
    # Method to display book information
    def display_info(self):
        print(f"Book Name: {self.__book_name}")
        print(f"Author: {self.__author}")
        availability = "Available" if self.__available else "Not Available"
        print(f"Availability: {availability}")

# Testing the LibraryBook class
if __name__ == "__main__":
    # Creating instances of LibraryBook class
    book1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = LibraryBook("To Kill a Mockingbird", "Harper Lee")
    
    # Displaying initial information
    print("Initial Information:")
    book1.display_info()
    book2.display_info()
    print()
    
    # Borrowing book1
    book1.borrow_book()
    
    # Trying to borrow book1 again
    book1.borrow_book()
    
    # Returning book1
    book1.return_book()
    
    # Displaying updated information
    print("\nUpdated Information:")
    book1.display_info()
    book2.display_info()
