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
        super().__init__()

    def calculate_point():
        pass
