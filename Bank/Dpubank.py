from bank import Bank


class DpuBank(Bank):
    def __init__(self, bank_name, loan_amount, loan_year, loan_rate):
        super().__init__(bank_name)
        self.loan_amount = loan_amount
        self.loan_year = loan_year
        self.loan_rate = loan_rate
        self.interest = 0
        self.monthly_pay = 0

    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        if value < 0:
            raise ValueError("Loan amount must be non-negative")
        self._loan_amount = value

    @property
    def loan_year(self):
        return self._loan_year

    @loan_year.setter
    def loan_year(self, value):
        if value < 0:
            raise ValueError("Loan amount must be non-negative")
        self._loan_year = value

    @property
    def loan_rate(self):
        return self._loan_rate

    @loan_rate.setter
    def loan_rate(self, value):
        if value < 0:
            raise ValueError("Loan amount must be non-negative")
        self._loan_rate = value

    def flat_rate(self):
        """คำนวณดอกเบี้ยและจำนวนเงินที่ต้องชำระในแต่ละงวด"""
        self.interest = self.loan_amount * self.loan_rate * self.loan_year / 100
        self.monthly_pay = (self.loan_amount +
                            self.interest) / (self.loan_year * 12)

    def display_interest(self):
        """แสดงรายละเอียดของการกู้เงิน"""
        print(
            f"#####################  {self.bank_name} Loan Info  ###################")
        print(f"Loan: {self.loan_amount:,.2f} Bath")
        print(f"Rate: {self.loan_rate:.2f}%")
        print(f"Year: {self.loan_year}")
        print(f"Interest: {self.interest:,.2f} Baht")
        print(f"Monthly Repayment: {self.monthly_pay:,.2f} Baht")


# สร้างวัตถุสำหรับการคิดดอกเบี้ยของธนาคาร DPU
dpubank = DpuBank("DPU Bank", 100000, 2, 3)

# คำนวณดอกเบี้ยและจำนวนเงินที่ต้องชำระในแต่ละงวด
dpubank.flat_rate()

# แสดงรายละเอียดของการกู้เงิน
dpubank.display_interest()
