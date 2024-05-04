from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand: str, speed: int, gear: int, seat: int,capacity:int,wheel:int) -> None:
        super().__init__(brand, speed, gear, seat)
        self.capacity = capacity
        self.wheel = wheel

    
    def show_detail(self):
        print(f'                      ')
        print(f'++++ {type(self).__name__} Detail ++++ ')
        print(f'{self.brand} with speed {self.speed} km/hr and {self.gear} can carry {self.capacity} tons')
    def show_price(self):
        print(f'                      ')
        price = self.wheel * 250
        print(f'++++ {type(self).__name__} Detail ++++')
        print(f'{self.wheel} wheels truck is {price} bath/day')
        print(f'                      ')


if __name__ == '__main__':
    test=Truck('IZUSU',150,4,4,1000,8)
    test.show_detail()
    test.show_price()