from models import Book

class Library:
    def __init__(self):
        self.books = []  # Stores all books in the library

    def add_book(self, book):
        self.books.append(book)
        print(f"📖 Book '{book.title}' added to the library.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"❌ Book '{book.title}' removed from the library.")
                return
        print("⚠️ Book not found.")

    def list_books(self):
        print("\n📚 Available Books in the Library:")
        for book in self.books:
            print(book)