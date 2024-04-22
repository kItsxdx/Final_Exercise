#6611375 กฤษดา ขันตรี
class JuiceOrder:
    def __init__(self, menu, size):
        self.menu = menu
        self.size = size
        self.price = None

    def check_menu(self):
        menu_options = {
            "OJ": 25,  # Orange 
            "AJ": 25,  # Apple 
            "WJ": 30,  # Watermelon 
            "PJ": 30   # Pineapple 
        }

        if self.menu not in menu_options:
            raise ValueError(f"ไม่มีเมนูนี้: {self.menu}")

        self.price = menu_options[self.menu]

    def compute_price(self):
        if self.size == "L":
            self.price += 5

    def display_order(self):
        print(f"{self.menu} ({self.size} * {self.price})=>{self.price} baht")


