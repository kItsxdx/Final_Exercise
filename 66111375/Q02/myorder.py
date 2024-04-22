#6611375 กฤษดา ขันตรี
from juicemanchine import JuiceOrder

def main():
    
    order1 = JuiceOrder("WJ", "L")
    order2 = JuiceOrder("OJ", "R")
    order3 = JuiceOrder("PJ", "L")

    
    for order in [order1, order2, order3]:
        try:
            order.check_menu()
            order.compute_price()
            order.display_order()
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()