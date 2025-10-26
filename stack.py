# stack.py

# -----------------------------
# Transaction Node for Stack
# -----------------------------
class Transaction:
    def __init__(self, action, book_id):
        self.action = action  # "Issue" or "Return"
        self.book_id = book_id
        self.next = None


# -----------------------------
# Stack for Undo Functionality
# -----------------------------
class TransactionStack:
    def __init__(self):
        self.top = None

    def push(self, action, book_id):
        new_trans = Transaction(action, book_id)
        new_trans.next = self.top
        self.top = new_trans

    def pop(self):
        if self.top is None:
            return None
        popped = self.top
        self.top = self.top.next
        return popped

    def is_empty(self):
        return self.top is None

    def view_transactions(self):
        if self.top is None:
            print("📂 No recent transactions.")
            return
        print("\n🧾 Recent Transactions:")
        temp = self.top
        while temp:
            print(f"{temp.action} Book ID: {temp.book_id}")
            temp = temp.next
        print()
