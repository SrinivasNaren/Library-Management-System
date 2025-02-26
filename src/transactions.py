from datetime import datetime, timedelta

class BorrowTransaction:
    def __init__(self, book, member):
        if book.is_available:
            self.book = book
            self.member = member
            self.borrow_date = datetime.now()
            self.due_date = self.borrow_date + timedelta(days=14)
            book.is_available = False  # Mark the book as borrowed
            print(f"✅ '{book.title}' borrowed by {member}. Due Date: {self.due_date.strftime('%Y-%m-%d')}")
        else:
            print(f"⚠️ Sorry, '{book.title}' is already borrowed!")

    def return_book(self, return_date):
        self.book.is_available = True  # Mark book as available
        fine = self.calculate_fine(return_date)
        print(f"✅ '{self.book.title}' returned by {self.member}. Fine: ₹{fine}")

    def calculate_fine(self, return_date):
        days_late = (return_date - self.due_date).days
        return max(days_late * 5, 0) if days_late > 0 else 0