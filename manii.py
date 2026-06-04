# class Bank:
#     def __init__(self):
#         self.__balance = 1
#     def deposit(self, amount):
#         self.__balance += amount
#     def show_balance(self):
#         print("balance:", self.__balance)
# b = Bank()
# b.deposit(500)
# b.show_balance()

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_available = True
    
#     def __str__(self):
#         status = "Available" if self.is_available else "Issued"
#         return f"{self.title} by {self.author} [{status}]"
    
# class Library:
#     def __init__(self):
#         self.books = []
#     def add_books(self, book):
#         self.books.append(book)
#         print(f"Book'{book.title}' added to the library")
#     def display_books(self):
#         if not self.books:
#             print("No books in the library.")
#         for book in self.books:
#             print(book)

#     def borrow_book(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower() and book.is_available:
#                 book.is_available = False
#                 print(f"You have borrowed'{book.title}")
#                 return
#             print("Book not available or already issued")
    
#     def return_book(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower() and not book.is_available:
#                 book.is_available == True
#                 print(f"You have returned '{book.title}.")
#                 return
#             print("This book was not borrowed or dosen't exist.")

# lib = Library()

# lib.add_books(Book("The Alchemist", "Paulo Coelho"))
# lib.add_books(Book("1984", "George Orwell"))
# lib.add_books(Book("Python 101", "Michael Driscoll"))
# print("Available Books.")
# lib.display_books()

# print("Borrowing '1984:")
# lib.borrow_book("1984")

# print("Borrowing '1984' again:")
# lib.borrow_book("1984")

# print("Returning '1984':")
# lib.return_book("1984")

# print("Final Book List:")
# lib.display_books()
     