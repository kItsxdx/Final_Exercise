from abc import ABC
class Vehicle(ABC):
    def __init__(self,brand:str,speed:int,gear:int,seat:int) -> None:
        super().__init__()
        self.brand = brand
        self.speed =speed
        self.gear = gear
        self.seat = seat


    def show_detail(self):
        print(f'===== {type(self).__name__} Detail =====')
        print(f'{self.brand} with speed {self.speed} km/hr manufactured in {self.year} has {self.gear} and {self.seat} seats' )


