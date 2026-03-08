class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self._isbn = isbn
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print(self.title, "was borrowed.")
        else:
            print(self.title, "is not available.")

    def return_book(self):
        self.available = True
        print(self.title, "was returned.")

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, isbn, format_type):
        super().__init__(title, author, isbn)
        self.format_type = format_type

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, Format: {self.format_type}"


class Student:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow(self, book):
        if book.available:
            book.borrow_book()
            self.books.append(book)
        else:
            print(self.name, "could not borrow", book.title)

    def show_books(self):
        print(self.name, "has borrowed:")
        for book in self.books:
            print("-", book.title)

    def __str__(self):
        return f"Student: {self.name}"


def main():
    book1 = Book("The Hobbit", "J.R.R. Tolkien", "1111")
    book2 = Book("1984", "George Orwell", "2222")
    ebook1 = EBook("Python Basics", "John Smith", "3333", "PDF")

    student1 = Student("Derek")

    print(book1)
    print(book2)
    print(ebook1)
    print(student1)
    print()

    student1.borrow(book1)
    student1.borrow(ebook1)
    print()

    student1.show_books()
    print()

    book1.return_book()


main()