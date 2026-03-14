class MoneyNotEnoughError(Exception):
    """Raised when there are insufficient funds for the transaction."""
    pass

class PINCodeError(Exception):
    """Raised when the entered PIN code is incorrect."""
    pass

class UnderageTransactionError(Exception):
    """Raised when a user under 18 attempts a transaction."""
    pass

class MoneyIsNegativeError(Exception):
    """Raised when a negative amount is provided."""
    pass

pin_code, balance, age = input().split(", ")
pin_code = pin_code.strip()
balance = float(balance.strip())
age = int(age.strip())

while True:
    command = input()
    if command == "End":
        break

    try:
        if command.startswith("Send Money#"):
            _, amount, entered_pin = command.split("#")
            amount = float(amount.strip())
            entered_pin = entered_pin.strip()

            if entered_pin != pin_code:
                raise PINCodeError("Invalid PIN code")

            if age < 18:
                raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

            if amount > balance:
                raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

            balance -= amount
            print(f"Successfully sent {amount:.2f} money to a friend")
            print(f"There is {balance:.2f} money left in the bank account")

        elif command.startswith("Receive Money#"):
            _, amount = command.split("#")
            amount = float(amount.strip())

            if amount < 0:
                raise MoneyIsNegativeError("The amount of money cannot be a negative number")

            balance += amount / 2
            print(f"{amount / 2:.2f} money went straight into the bank account")

    except (MoneyNotEnoughError, PINCodeError, UnderageTransactionError, MoneyIsNegativeError) as e:
        print(e)
