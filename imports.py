import time
import pytest
from class_ex import Motorcycle, Car

print(Motorcycle)

car = Car('Honda', 'civic')
moto = Motorcycle('Hero', 'Honda')  # instance of class=moto

for vehicle in [moto, car]:
    print(f'The time is {time.time()}')
    print(vehicle)
    vehicle.turn_engine_on()
    vehicle.turn_headlight_on()
    vehicle.start_driving()
    vehicle.turn('left')
    vehicle.turn('right')
    vehicle.stop_driving()
    vehicle.turn_engine_off()
    vehicle.turn_headlight_off()
    print()
    time.sleep(1)
#pytest
