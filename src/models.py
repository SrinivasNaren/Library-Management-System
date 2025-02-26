class Book:
    def __init__(self, book_id, title, author, isbn):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Track book availability

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.book_id}: {self.title} by {self.author} (ISBN: {self.isbn}) - {status}"