# book.py
from stack import TransactionStack

# -----------------------------
# Book Node (for Linked List)
# -----------------------------
class Book:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None


# -----------------------------
# Linked List for Book Management
# -----------------------------
class BookList:
    def __init__(self):
        self.head = None

    def insert_book(self, book_id, title, author):
        new_book = Book(book_id, title, author)
        if self.head is None:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print("✅ Book inserted successfully!")

    def delete_book(self, book_id):
        if self.head is None:
            print("⚠️ No books available.")
            return

        if self.head.book_id == book_id:
            self.head = self.head.next
            print("✅ Book deleted successfully!")
            return

        prev = None
        curr = self.head
        while curr and curr.book_id != book_id:
            prev = curr
            curr = curr.next

        if curr is None:
            print("❌ Book not found.")
            return

        prev.next = curr.next
        print("✅ Book deleted successfully!")

    def search_book(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                return temp
            temp = temp.next
        return None

    def display_books(self):
        if self.head is None:
            print("📚 No books in the library.")
            return

        print("\n📖 Current Book List:")
        temp = self.head
        while temp:
            print(
                f"Book ID: {temp.book_id} | Title: {temp.title} | "
                f"Author: {temp.author} | Status: {temp.status}"
            )
            temp = temp.next
        print()

    # -----------------------------
    # Transaction Operations
    # -----------------------------
    def issue_book(self, book_id, stack: TransactionStack):
        book = self.search_book(book_id)
        if not book:
            print("❌ Book not found!")
            return
        if book.status == "Issued":
            print("⚠️ Book already issued.")
            return
        book.status = "Issued"
        stack.push("Issue", book_id)
        print("✅ Book issued successfully!")

    def return_book(self, book_id, stack: TransactionStack):
        book = self.search_book(book_id)
        if not book:
            print("❌ Book not found!")
            return
        if book.status == "Available":
            print("⚠️ Book is already available.")
            return
        book.status = "Available"
        stack.push("Return", book_id)
        print("✅ Book returned successfully!")

    def undo_transaction(self, stack: TransactionStack):
        if stack.is_empty():
            print("⚠️ No transactions to undo.")
            return

        last = stack.pop()
        book = self.search_book(last.book_id)
        if not book:
            print("❌ Book not found for undo operation.")
            return

        if last.action == "Issue":
            book.status = "Available"
            print("↩️ Undo successful: Book returned to library.")
        elif last.action == "Return":
            book.status = "Issued"
            print("↩️ Undo successful: Book re-issued.")
