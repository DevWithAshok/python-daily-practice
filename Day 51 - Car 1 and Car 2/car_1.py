class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        
    def max_speed(self,max_speed):
        self.max_speed=max_speed
        
    def acceleration(self,acceleration):
        self.acceleration=acceleration
        
    def tyre_friction(self,tyre_friction):
        self.tyre_friction=tyre_friction


def default_test():
 car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
 print(car.color)
 print(car.max_speed)
 print(car.acceleration)
 print(car.tyre_friction)
