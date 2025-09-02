class InsufficientFundsError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

class AccountLockedError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Holder: {self.account_holder}, Balance: {self.balance:.2f}"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self.balance

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=1000.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive")
        if amount > (self.balance + self.overdraft_limit):
            raise InsufficientFundsError("Exceeds overdraft limit")
        self.balance -= amount
        return self.balance

class FixedDepositAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, lock_in_period=12):
        super().__init__(account_number, account_holder, balance)
        self.lock_in_period = lock_in_period
        self.months_active = 0

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive")
        if self.months_active < self.lock_in_period:
            raise AccountLockedError(f"Account is locked for {self.lock_in_period - self.months_active} more months")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount
        return self.balance

    def increment_month(self):
        self.months_active += 1

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def transfer_funds(self, from_account_number, to_account_number, amount):
        if amount <= 0:
            raise NegativeAmountError("Transfer amount must be positive")
        if from_account_number not in self.accounts or to_account_number not in self.accounts:
            raise ValueError("Invalid account number")
        from_account = self.accounts[from_account_number]
        to_account = self.accounts[to_account_number]
        from_account.withdraw(amount)
        to_account.deposit(amount)
        return f"Transferred {amount:.2f} from {from_account_number} to {to_account_number}"

def main():
    try:
        bank = Bank()
        savings = SavingsAccount("SA001", "Adhithiya", 1000.0, 0.03)
        current = CurrentAccount("CA001", "Vyshag", 500.0, 1000.0)
        fixed = FixedDepositAccount("FD001", "Chole", 2000.0, 6)
        bank.add_account(savings)
        bank.add_account(current)
        bank.add_account(fixed)
        print(savings)
        savings.deposit(500.0)
        print(f"After deposit: {savings}")
        savings.withdraw(200.0)
        print(f"After withdrawal: {savings}")
        savings.apply_interest()
        print(f"After interest applied: {savings}")
        print(current)
        current.deposit(300.0)
        print(f"After deposit: {current}")
        current.withdraw(1200.0)
        print(f"After withdrawal (overdraft): {current}")
        print(fixed)
        fixed.deposit(1000.0)
        print(f"After deposit: {fixed}")
        try:
            fixed.withdraw(500.0)
        except AccountLockedError as e:
            print(f"Error: {e}")
        fixed.increment_month()
        fixed.increment_month()
        fixed.increment_month()
        fixed.increment_month()
        fixed.increment_month()
        fixed.increment_month()
        fixed.withdraw(500.0)
        print(f"After withdrawal (post lock-in): {fixed}")
        print(bank.transfer_funds("SA001", "CA001", 300.0))
        print(f"Savings after transfer: {savings}")
        print(f"Current after transfer: {current}")
        try:
            savings.deposit(-100.0)
        except NegativeAmountError as e:
            print(f"Error: {e}")
        try:
            current.withdraw(2000.0)
        except InsufficientFundsError as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()