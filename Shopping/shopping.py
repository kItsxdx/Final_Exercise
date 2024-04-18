class Item:
    def __init__(self, item: str, price: float):
        self.item = item
        self.price = price


"""
    ฟังก์ชันสร้างวัตถุ Item

    Args:
      item: ชื่อสินค้า
      price: ราคาสินค้า
    """


class MemberCard:
    """
  คลาสสำหรับจัดเก็บข้อมูลเกี่ยวกับบัตรสมาชิกของร้านประเภททั่วไป
  """

    def __init__(self):
        """
    ฟังก์ชันสร้างวัตถุ MemberCard
    """
        self.ctype = "Member Card"
        self.cart = []
        self.point = 0

    def add_item(self, item, price):
        """ฟังชันเพิ่มสินค้าลงในตะกร้าสินค้า
        Arge:
            item: ชื่อสินค้า
            price: ราคาสินค้า
        """
        self.cart.append(Item(item, price))

    def calculate_point(self):
        """ฟังชั่นคำนวณคะแนนที่ได้รับจากการใช้จ่าย
            Return:
                คะแนนที่ได้รับจากการใช้จ่าย        
        """
        for item in self.cart:
            self.point += item.price // 40


class PlatinumCard(MemberCard):
    """คลาสสำหรับจัดเก็บข้อมูลเกี่ยวกับบัตรสมาชิกของร้านประเภท platinum"""

    def __init__(self):
        """ฟังชันสร้างวัตถุ PlatinumCard"""

        super().__init__()
        self.ctype = "Platinum Card"

    def calculate_point(self):
        """ฟังชันคำนวณคะแนนที่ใช้จ่าย
        Return:
            คะแนนที่ได้รับจากการใช้จ่ายฃ
        """
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
