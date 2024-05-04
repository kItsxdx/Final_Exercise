#bank.py
from abc import ABC, abstractmethod
#Abstract Class
class Bank(ABC):
    #Flat Rate
    def __init__(self,bankname:str) -> None:
        super().__init__()
        self.bankname = bankname

    @abstractmethod #Abstarct Method
    def flat_rate(self):
       pass
----------------------------------------------
from bank import Bank
class DpuBank(Bank):
    def __init__(self, bankname) -> None:
        super().__init__(bankname)
        self.__loanamount = 0
        self.__loanyear= 0
        self.__loanrate = 0
        self.interest = 0
        self.monthlypay = 0
    
    @property
    def loanamount(self):
        return self.__loanamount
    
    @loanamount.setter
    def loanamount(self,value):
        self.__loanamount = value
    
    @property
    def loanrate(self):
        return self.__loanrate

    @loanrate.setter
    def loanrate(self,value):
        self.__loanrate = value

    @property
    def loanyear(self):
        return self.__loanyear
    
    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value
    
    def flat_rate(self):
       super().flat_rate()
       self.interest = self.loanamount * (self.loanrate / 100) * self.loanyear
       self.monthlypay = (self.loanamount + self.interest) / (self.loanyear * 12)
    
    def display_interest(self):
        print(f'****** {self.bankname} Bank Loan Info ******')
        print(f'Loan: {self.loanamount:,.2f} baht')
        print(f'Rate: {self.loanrate:.2f}%')
        print(f'Year: {self.loanyear}')
        print('-- Interest --')
        print(f'Interest: {self.interest:,.2f} baht')
        print(f'Monthly Repayment: {self.monthlypay:,.2f} baht')

if __name__ == '__main__':
    cus = DpuBank('DPU')
    cus.loanamount = 100000
    cus.loanrate = 3
    cus.loanyear = 2
    cus.flat_rate()
    cus.display_interest()