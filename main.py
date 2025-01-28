import json

# Step 1: Define the BudgetTracker class
class BudgetTracker:
    def __init__(self, filename):
        self.balance = 0                            # Total amount of money
        self.transactions = []                      # list that will store details of income and expenses
        self.category = ""                          # Cateogry of transaction
        self.filename = filename                    # name of file in which all data stored
        self.load_transactions()                    # Load all data before initializing, and create file if not found

# Step 2: Implement the add_income method
    def add_income(self, amount, description, category = "None"):
        self.balance += amount
        self.transactions.append(("Income", amount, description, category))
        self.save_transactions()

    def add_expense(self, amount, description, category = "None"):
        if self.balance <= amount:
            print("Warning! Insufficient balance.")

        self.balance -= amount
        self.transactions.append(("Expense", amount, description, category))
        self.save_transactions()

    def show_summary(self):
        print(f"Transactions:\n")
        for transaction_type, amount, description, category in self.transactions:
            print(f"{transaction_type} | ${amount} | {description} | {category}")
        print(f"\nTotal Balance: ${self.balance}.")

    def save_transactions(self):
        with open(file= self.filename, mode= "w") as file:
            json.dump(obj= self.transactions, fp= file, indent= 2)

    def load_transactions(self):
        try:
            with open(file= self.filename, mode= "r") as file:
                self.transactions = json.load(fp= file)
        except FileNotFoundError:
            with open(file= self.filename, mode= "w") as file:
                json.dump(obj= {}, fp= file, indent= 2)

tracker = BudgetTracker(filename= "data.json")

tracker.add_income(amount=5000, description="Salary")
tracker.add_expense(amount=2000, description="Rent", category= "Home")
tracker.add_expense(amount=500, description="Groceries", category= "Grocery")

tracker.show_summary()