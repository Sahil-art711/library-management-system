# main.py
from book import BookList
from stack import TransactionStack

def main():
    library = BookList()
    transactions = TransactionStack()

    while True:
        print("\n========== 📚 Library Book Management System ==========")
        print("1. Insert Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Undo Last Transaction")
        print("8. View Transactions")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                library.insert_book(book_id, title, author)
            except ValueError:
                print("❌ Invalid input. Book ID must be an integer.")

        elif choice == "2":
            try:
                book_id = int(input("Enter Book ID to delete: "))
                library.delete_book(book_id)
            except ValueError:
                print("❌ Invalid input. Book ID must be an integer.")

        elif choice == "3":
            try:
                book_id = int(input("Enter Book ID to search: "))
                book = library.search_book(book_id)
                if book:
                    print(
                        f"✅ Book Found: {book.title} by {book.author} | Status: {book.status}"
                    )
                else:
                    print("❌ Book not found.")
            except ValueError:
                print("❌ Invalid input. Book ID must be an integer.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            try:
                book_id = int(input("Enter Book ID to issue: "))
                library.issue_book(book_id, transactions)
            except ValueError:
                print("❌ Invalid input. Book ID must be an integer.")

        elif choice == "6":
            try:
                book_id = int(input("Enter Book ID to return: "))
                library.return_book(book_id, transactions)
            except ValueError:
                print("❌ Invalid input. Book ID must be an integer.")

        elif choice == "7":
            library.undo_transaction(transactions)

        elif choice == "8":
            transactions.view_transactions()

        elif choice == "9":
            print("👋 Exiting program...")
            break

        else:
            print("⚠️ Invalid choice! Try again.")


if __name__ == "__main__":
    main()
