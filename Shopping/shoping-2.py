#shopping.py
#inheritance
#https://programming-21.mooc.fi/part-10/1-class-hierarchies
from math import floor
class Item:
    def __init__(self,item:str,price:float) -> None:
        self.item = item
        self.price = price

class MemberCard:
    def __init__(self) -> None:
        self.cart = []
        self.point = 0
        self.ctype = 'Member Card'

    def add_item(self, item: Item):
        self.cart.append(item)
    
    def calculate_point(self):
        # ทุกๆ การใช้จ่าย 40 บาท จะได้รับคะแนน 1 คะแนน
        totalprice = 0
        for product in self.cart:
            totalprice = totalprice + product.price
        
        self.point = floor(self.point + (totalprice / 40))
        
        print(f'วันนี้ใช้จ่ายทั้งหมด: {totalprice:,.2f} บาท')
        print(f'คะแนนจากการใช้จ่ายวันนี้: {self.point:,.2f} คะแนน')

class PlatinumCard(MemberCard):
    def __init__(self) -> None:
        super().__init__()
        self.ctype = 'Platinum Card'

    def calculate_point(self):
        # ทุกๆ การใช้จ่าย 25 บาท จะได้รับคะแนน 1 คะแนน
        totalprice = 0
        for product in self.cart:
            totalprice = totalprice + product.price
        
        self.point = floor(self.point + (totalprice / 25))
        
        print(f'วันนี้ใช้จ่ายทั้งหมด: {totalprice:,.2f} บาท')
        print(f'คะแนนจากการใช้จ่ายวันนี้: {self.point:,.2f} คะแนน')
    

if __name__ == '__main__':
    cus1 = MemberCard()
    cus1.add_item(Item("นม", 45))
    cus1.add_item(Item("ขนมปัง", 23))
    cus1.add_item(Item("เนยถั่ว", 70))
    print(f'------ {cus1.ctype} ------')
    cus1.calculate_point()

    print()

    cus2 = PlatinumCard()
    cus2.add_item(Item("พิซซ่า", 200))
    cus2.add_item(Item("น้ำอัดลม", 35))
    cus2.add_item(Item("มันฝรั่งทอด", 60))
    print(f'------ {cus2.ctype} ------')
    cus2.calculate_point() 