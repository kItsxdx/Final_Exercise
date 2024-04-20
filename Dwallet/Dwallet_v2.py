# Dwallet_v2
class DigitalWallet_v2:
    def __init__(self, ewallet_no, cid, cname, balance=0.0):
        self.ewallet_no = ewallet_no
        self.cid = cid
        self.cname = cname
        self.balance = balance
# methods การฝากเงิน

    def deposit(self, amount):
        min_deposit_amount = 100.0

        if amount >= min_deposit_amount:
            self.balance += amount
            message = f'ฝากเงินสำเร็จ {amount:.2f} bath. ยอดเงินคงเหลือ {self.balance:.2f}bath.'
        else:
            message = f"ฝากขั้นต้ำ 100 บาท"
        return message
# methods การถอนเงิน

    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            return f'การถอนเงินสำเร็จ: {amount:.2f}บาท  ยอดเงินคงเหลือ: {self.balance:.2f}บาท'
        else:
            return 'ยอดเงินคงเหลือไม่พอสำหรับการถอน'
# methods การเปลี่ยนชื่อ

    def change_name(self, new_name):
        self.cname = new_name
        return f'เปลี่ยนชื่อลูกค้าเป็นชื่อ {new_name} เรียบร้อย. '


# ตัวอย่างการใช้งาน
wallet = DigitalWallet_v2('123-456', '1-11-2345-99', 'สมชาย', 1000)

# ตัวอย่างการฝากเงิน
deposit_amount = float(input('กรอกจำนวนเงินที่ฝาก:'))
message = wallet.deposit(deposit_amount)
print(message)

# ตัวอย่างการเปลี่ยนชื่อ
new_name = input('กรอกชื่อใหม่ของท่าน:')
message = wallet.change_name(new_name)
print(message)

# ตัวอย่างการถอนเงิน
withdraw_amount = float(input('กรอกจำนวนเงินที่จะถอน:'))
message = wallet.withdraw(withdraw_amount)
print(message)
