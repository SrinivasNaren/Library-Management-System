from models import Book
from library import Library
from transactions import BorrowTransaction
from datetime import datetime, timedelta

# Initialize Library
library = Library()

# Add Books
book1 = Book(1, "Python Crash Course", "Eric Matthes", "1234567890")
book2 = Book(2, "Design Patterns", "Erich Gamma", "0987654321")
library.add_book(book1)
library.add_book(book2)

# List Books
library.list_books()

# Borrow a Book
transaction = BorrowTransaction(book1, "Alice")

# Try Borrowing the Same Book Again (Should Fail)
transaction2 = BorrowTransaction(book1, "Bob")

# Return Book (5 Days Late)
return_date = datetime.now() + timedelta(days=19)
transaction.return_book(return_date)

# List Books Again
library.list_books()