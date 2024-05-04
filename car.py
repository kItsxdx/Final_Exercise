from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand: str, speed: int, gear: int, seat: int,year:int,maintenance:int) -> None:
        super().__init__(brand, speed, gear, seat)
        self.year = year
        self.maintenance = maintenance

    
    def show_detail(self):
        print(f'                    ')
        print(f'===={type(self).__name__} detail ====')
        print(f'{self.brand} with speed {self.speed} km/hr manufactured in {self.year} has {self.gear} and {self.seat} seats' )

    def show_maintenance(self):
        print(f'                    ')
        print(f'===== {type(self).__name__}  Maintenance ====')
        print(f'The latest {self.brand} : {self.year} maintenance in {self.maintenance}')

if __name__ == '__main__':
    test=Car('Toyota',200,7,4,2019,2021)
    test.show_detail()
    test.show_maintenance()