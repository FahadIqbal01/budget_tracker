# Step 1: Define the BudgetTracker class
class BudgetTracker:
    def __init__(self):
        self.balance = 0                            # Total amount of money
        self.transactions = []                      # list that will store details of income and expenses
        self.category = ""                          # Cateogry of transaction

# Step 2: Implement the add_income method
    def add_income(self, amount, description, category = "None"):
        self.balance += amount
        self.transactions.append(("Income", amount, description, category))

    def add_expense(self, amount, description, category = "None"):
        if self.balance <= amount:
            print("Warning! Insufficient balance.")

        self.balance -= amount
        self.transactions.append(("Expense", amount, description, category))

    def show_summary(self):
        print(f"Transactions:\n")
        for transaction_type, amount, description, category in self.transactions:
            print(f"{transaction_type}: ${amount} - {description} - {category}")
        print(f"\nTotal Balance: ${self.balance}.")


tracker = BudgetTracker()

tracker.add_income(amount=5000, description="Salary")
tracker.add_expense(amount=2000, description="Rent", category= "Home")
tracker.add_expense(amount=500, description="Groceries", category= "Grocery")

tracker.show_summary()