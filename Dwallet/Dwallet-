#dwallet.py
#encapsulation
#https://programming-21.mooc.fi/part-9/3-encapsulation
class DigitalWallet:
    def __init__(self,ewallet_no:str, cid:str, cname:str, balance:float=0) -> None:
        self.__ewallet_no = ewallet_no
        self.__cid = cid
        self.__cname: cname
        self.__balance = balance
    
    def deposit(self, amount:float):
        if amount >= 100:
            self.__balance = self.__balance + amount
            print(f'คุณฝากเงินจำนวน: {amount:,.2f} บาท')
            self.check_balance()
        else:
            print('กรุณาเติมเงินเข้ากระเป๋าขั้นต่ำ 100 บาท')

    def withdraw(self, amount:float):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance -  amount
            print(f'คุณถอนเงินจำนวน: {amount:,.2f} บาท')
            self.check_balance()
        else:
            print(f'จำนวนเงินในกระเป๋าไม่เพียงพอต่อการถอนเงิน {amount:,.2f} บาท')
            self.check_balance()

    def check_balance(self):
        print(f'เงินคงเหลือในบัญชี : {self.__balance:,.2f} บาท')
    
    @property
    def cname(self):
        return self.__cname
    @cname.setter
    def cname(self,cname:str):
        self.__cname = cname

if __name__ == '__main__':
    dwobj = DigitalWallet('123-456','1-1234-45678-01-2','Bobby Parker',100)

    dwobj.deposit(200)
    
    dwobj.cname = 'Peter Parker'

    print(f'ชื่อบัญชี: {dwobj.cname}')

    dwobj.withdraw(500)

    dwobj.withdraw(100)
    