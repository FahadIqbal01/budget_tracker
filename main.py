import json

# Step 1: Define the BudgetTracker class
class BudgetTracker:
    def __init__(self, filename):
        self.balance = 0                            # Total amount of money
        self.transactions = []                      # list that will store details of income and expenses
        self.filename = filename                    # name of file in which all data stored
        self.load_transactions()                    # Load all data before initializing, and create file if not found

# Step 2: Implement the add_income method
    def add_income(self, amount, description, category = "None"):
        self.balance += amount
        self.transactions.append(
            {
                "type" : "Income", 
                "amount" : amount, 
                "description" : description, 
                "category" :category
            }
        )
        self.save_transactions()

    def add_expense(self, amount, description, category = "None"):
        if self.balance <= amount:
            print("Warning! Insufficient balance.")

        self.balance -= amount
        self.transactions.append(
            {
                "type" : "Expense", 
                "amount" : amount,
                "description" : description,
                "category" : category
            }
        )
        self.save_transactions()

    def show_summary(self):
        print(f"Transactions:\n")
        for transaction in self.transactions:
            print(f"{transaction["type"]} | {transaction["amount"]} | {transaction["description"]} | {transaction["category"]}")
        print(f"\nTotal Balance: ${self.balance}.")

    def save_transactions(self):
        data = {
            "balance" : self.balance,
            "transaction": self.transactions
        }
        with open(file= self.filename, mode= "w") as file:
            json.dump(obj= data, fp= file, indent= 2)

    def load_transactions(self):
        try:
            with open(file= self.filename, mode= "r") as file:
                data = json.load(fp= file)
                self.balance = data["balance"]
                self.transactions = data["transaction"]
        except FileNotFoundError:
            with open(file= self.filename, mode= "w") as file:
                json.dump(obj= {}, fp= file, indent= 2)

tracker = BudgetTracker(filename= "data.json")

tracker.add_income(amount=5000, description="Salary", category= "Income")
tracker.add_expense(amount=2000, description="Rent", category= "Home")
tracker.add_expense(amount=500, description="Groceries", category= "Grocery")

tracker.show_summary()