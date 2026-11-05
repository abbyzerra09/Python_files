class BankAccount:
    bank_name = "XYZ Bank"
    next_account_id = 1000

    def __init__(self, account_holder, balance):
        # give each account its own id then move the counter on
        self.id = BankAccount.next_account_id
        BankAccount.next_account_id = BankAccount.next_account_id + 1
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.account_holder} deposited £{amount}. New balance: £{self.balance}.")

    def withdraw(self, amount):
        # can't take out more than what's in the account
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance = self.balance - amount
            print(f"{self.account_holder} withdrew £{amount}. New balance: £{self.balance}.")

    def display_info(self):
        print(f"{self.bank_name} | ID: {self.id}, Balance: £{self.balance} | Holder: {self.account_holder}.")


if __name__ == "__main__":
    # Creating instances of the BankAccount class.
    alice_account = BankAccount(account_holder="Alice Khan", balance=1000)
    bob_account = BankAccount(account_holder="Bob Smith", balance=500)

    # Modifying instance attribute.
    alice_account.withdraw(200)
    bob_account.deposit(200)

    # Modifying class attribute (affects all instances).
    BankAccount.bank_name = "ABC Bank"

    # Displaying updated information.
    alice_account.display_info()
    bob_account.display_info()