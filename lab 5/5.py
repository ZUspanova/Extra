class Person:

    def __init__(self, fullname: str, age: int):
        self.fullname = fullname
        self.age = age

    def __str__(self):
        return f'{self.fullname}, he is {self.age} years old'

class Driver(Person):

    def __init__(self, fullname: str, age: int, expirience: int):
        super().__init__(fullname, age)
        self.expirience = expirience

    def __str__(self):
         return super().__str__() + f'\nHis expirience of driving is {self.expirience} years'


class Engine:

    def __init__(self,power,company):
        self.power=power
        self.company=company

    def __str__(self):
        return f'Engine has {self.power} h/p created by {self.company}'


class Car:

    def __init__(self,driver:Driver,engine:Engine,car_class:str,marka:str):
        self.driver=driver
        self.engine=engine
        self.car_class=car_class
        self.marka=marka

    def __str__(self):
        return f'Driver of this car is {self.driver}\n' \
               f'His car is {self.marka} {self.car_class}, {self.engine}'

    @staticmethod
    def start():
        print('Go')

    @staticmethod
    def stop():
        print('Stopping')

    @staticmethod
    def turn_right():
        print('Turning on the right')

    @staticmethod
    def turn_left():
        print('Turning on the left')

class Lorry(Car):

    def __init__(self,driver:Driver,engine:Engine,car_class:str,marka:str,carrying:int):
        super().__init__(driver,engine,car_class,marka)
        self.carrying=carrying

    def __str__(self):
        return super().__str__()+f'\nThis car has a load capacity of {self.carrying} tons'

class SportCar(Car):

    def __init__(self,driver:Driver,engine:Engine,car_class:str,marka:str,speed:float):
        super().__init__(driver,engine,car_class,marka)
        self.speed=speed

    def __str__(self):
        return super().__str__()+f'\nMax speed of this car is {self.speed} km/h'

driver=Driver(fullname='Ivan Ivanov',age=31,expirience=11)
engine=Engine(power=500,company='Mercedes')
lorry=Lorry(driver=driver,engine=engine,marka='Mercedes Benz',car_class='X-class',carrying=20)
print(lorry)
lorry.start()
lorry.turn_left()
lorry.turn_right()
lorry.stop()

print('-------------------------------------------------------------------')
second_driver=Driver('Michael Schumacher',age=53,expirience=31)
second_engine=Engine(power=800,company='Ferrari')
sportcar=SportCar(driver=second_driver,engine=second_engine,marka='Ferrari',car_class='S-class',speed=340)
print(sportcar)
