class LibraryCatalogue:
    library_name = "Default Library"
    next_book_id = 2000

    def __init__(self, title, author, genre, availability=True):
        self.__id = LibraryCatalogue.next_book_id
        LibraryCatalogue.next_book_id += 1

        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__availability = availability
        self.display_info()

    @classmethod
    def set_library_name(cls, library_name):
        print(f"{cls.library_name} name set to {library_name}")
        cls.library_name = library_name

    def checkout(self):
        self.__availability = False
        print(f"Book '{self.__title}' checked out successfully!")

    def return_book(self):
        self.__availability = True
        print(f"Book '{self.__title}' returned successfully!")

    def display_info(self):
        print(
            f"{LibraryCatalogue.library_name} | Id: {self.__id}, Title: '{self.__title}', Author: {self.__author}, Genre: {self.__genre}, Status: {"Available" if self.__availability else "Checked out"}")


if __name__ == "__main__":
    # Creating instances of the LibraryCatalog class.
    book1 = LibraryCatalogue(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction")
    book2 = LibraryCatalogue(title="To Kill a Mockingbird", author="Harper Lee", genre="Classics")

    # Modifying class attribute using class method.
    LibraryCatalogue.set_library_name("My Personal Library")

    # Modifying instance attribute.
    book1.checkout()

    # Displaying book information.
    book1.display_info()
    book2.display_info()
