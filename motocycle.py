from vehicle import Vehicle
class Motocycle(Vehicle):
    def __init__(self, brand: str, speed: int, gear: int, seat: int,cc: int, model:str) -> None:
        super().__init__(brand, speed, gear, seat)
        self._cc = cc
        self._model = model

    def show_detail(self):
        print(f'--- {type(self).__name__} ---')
        print(f'{self.brand} : {self._model} whit speed {self.speed} km/hr has cc :{self._cc}')
        print(f'')
if __name__ == '__main__':
    test = Motocycle('Honda',120,4,2,160,'New PCX')
    test.show_detail()