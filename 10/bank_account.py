#!/usr/bin/env python3

def safe_bank_operation(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except InsufficientFundsError as e:
            print(f"Error: {e}")
        except NegativeDepositError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except TypeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    return wrapper

class BankError(Exception):
    pass


class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Insufficient funds: balance ${balance}, attempted withdrawal ${amount}"
        )


class NegativeDepositError(BankError):
    def __init__(self, message):
        super().__init__(message)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @safe_bank_operation
    def deposit(self, amount):
        if amount <= 0:
            raise NegativeDepositError("Deposit amount must be positive")
        self.balance += amount
        print(
            f"Deposited ${amount} to {self.owner}'s account. New balance: {self.balance}"
        )

    @safe_bank_operation
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        self.balance -= amount
        print(
            f"Withdrew ${amount} from {self.owner}'s account. New balance: {self.balance}"
        )

    def show_balance(self):
        print(f"{self.owner}'s account balance: ${self.balance}")

