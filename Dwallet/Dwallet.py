class DigitalWallet:

    def __init__(self, ewallet_no: str, cid: str, cname: str, balance: float) -> None:
        self.ewallet_no = ewallet_no
        self.cid = cid
        self.cname = cname
        self.balance = balance

    def deposit(self, amount: float, balance):
        min_deposit_amount = 100
        if amount >= min_deposit_amount:
            self.balance += amount
            message = f'Successfullty deposited {amount}.New balance is {balance}'
        else:
            message = f'Deposit amount must be at least {min_deposit_amount}'
        return message

    def withdraw(self, amount: float, balance):

        if amount > 0 and amount < balance:
            balance -= amount
            return f'Withdraw Successful. Amount withdraw: {amount}. New balance: {balance}'
        else:
            return '****Insufficient balance for withdraw.****'

    def check_balance(self):
        self.deposit()
        self.withdraw()
        print(f'Your Amount: {self.balance}. Name:{self.cname}')


if __name__ == '__main__':
    cus1 = DigitalWallet(9999999, 77777777, 'GOD', 999999)
    cus1.check_balance
