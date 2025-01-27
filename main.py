# Step 1: Define the BudgetTracker class
class BudgetTracker:
    def __init__(self):
        self.balance = 0                            # Total amount of money
        self.transactions = []                      # list that will store details of income and expenses

# Step 2: Implement the add_income method
    def add_income(self, amount, description):
        self.balance += amount
        self.transactions.append(("Income", amount, description))

    def add_expense(self, amount, description):
        if self.balance <= amount:
            print("Warning! Insufficient balance.")

        self.balance -= amount
        self.transactions.append(("Expense", amount, description))

    def show_summary(self):
        print(f"Transactions:\n")
        for transaction_type, amount, description in self.transactions:
            print(f"{transaction_type}: ${amount} - {description}")
        print(f"\nTotal Balance: ${self.balance}.")


tracker = BudgetTracker()

tracker.add_income(amount=5000, description="Salary")
tracker.add_expense(amount=2000, description="Rent")
tracker.add_expense(amount=500, description="Groceries")
tracker.add_expense(amount=3000, description="Loan paid")

tracker.show_summary()