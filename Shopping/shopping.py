class Item:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
class MemberCard:
   
    def __init__(self):
       
        self.ctype = "Member Card"
        self.cart = []
        self.point = 0

    def add_item(self, item, price):
       
        self.cart.append(Item(item, price))

    def calculate_point(self):
       
        for item in self.cart:
            self.point += item.price // 40


class PlatinumCard(MemberCard):
    """คลาสสำหรับจัดเก็บข้อมูลเกี่ยวกับบัตรสมาชิกของร้านประเภท platinum"""

    def __init__(self):
        super().__init__()
        self.ctype = "Platinum Card"

    def calculate_point(self):
      
        for item in self.cart:
            self.point += item.price // 25


def main():
    """ฟังชันหลัก"""
    # สร้าง วัตถุ MemberCard
    member_card = MemberCard()

    # เพิ่มสินค้าลงในตะกร้าสินค้า
    member_card.add_item("นม", 45)
    member_card.add_item("ขนมปัง", 23)
    member_card.add_item("เนยถั่ว", 70)

    # คำนวณคะแนน
    member_card.calculate_point()

    # แสดงผล
    print(f"Member Card")
    print(
        f"วันนี้ใช้จ่ายทั่งหมด: {sum(item.price for item in member_card.cart):.2f} บาท")
    print(f"คะแนนจากการใช้จ่ายวันนี้:{member_card.point:.2f} คะแนน")

    # สร้างวัตถุ PlatinumCard
    platinum_card = PlatinumCard()

    # เพิ่มสินค้าในตะกร้า
    platinum_card.add_item("พิซซ่า", 200)
    platinum_card.add_item("น้ำอัดลม", 35)
    platinum_card.add_item("มันฝรั่งทอด", 60)

    # คำนวณคะแนน
    platinum_card.calculate_point()

    # แสดงผล
    print(f"\nPlatinum Card")
    print(
        f"วันนี้ใช้จ่ายทั้งหมด: {sum(item.price for item in platinum_card.cart):.2f}บาท")
    print(f"คะแนนจากการใช้จ่ายวันนี้: {platinum_card.point:.2f} คะแนน")


if __name__ == "__main__":
    main()

"""คำอธิบาย
โปรแกรมนี้ประกอบด้วยคลาส 3 คลาส ดังนี้

*คลาส Item: คลาสนี้ใช้สำหรับจัดเก็บข้อมูลสินค้า มีแอตทริบิวต์ 2 รายการ ได้แก่ item (ชื่อสินค้า) และ price (ราคาสินค้า)
*คลาส MemberCard: คลาสนี้ใช้สำหรับจัดเก็บข้อมูลเกี่ยวกับบัตรส
"""
