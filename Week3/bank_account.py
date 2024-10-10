class BankAccount:
    bank_name = "Default Bank Name"
    next_account_id = 1000

    def __init__(self, account_holder, balance):
        self.__id = BankAccount.next_account_id
        BankAccount.next_account_id += 1

        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"{self.__account_holder} deposited £{amount}. New balance: £{self.__balance}.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
            return

        self.__balance -= amount
        print(f"{self.__account_holder} withdrew £{amount}. New balance: £{self.__balance}.")

    def display_info(self):
        print(f"{self.bank_name} | ID: {self.__id}, Balance: £{self.__balance} | Holder: {self.__account_holder}.")


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
