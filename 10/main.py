#!/usr/bin/env python3

from bank_account import BankAccount, InsufficientFundsError, NegativeDepositError


def main():
    account = BankAccount("Aaron", 1000)

    account.show_balance()
    account.deposit(500)
    account.withdraw(30)
    account.deposit(-100)   # cause NegativeDepositError
    account.withdraw(5000)  # cause InsufficientFundsError
    account.show_balance()


if __name__ == "__main__":
    main()
