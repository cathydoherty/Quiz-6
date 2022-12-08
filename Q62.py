#Cathy Doherty
import math
class Ambulance:
    """Represents an ambulance.
       priority, speed, capacity"""

myambulance = Ambulance()
myambulance.priority = 0
myambulance.speed = 100
myambulance.capacity = 1

def controlled_velocity(car):
    velocity = -10*(1-car.priority) + 2.37 *(car.speed/10)**3.98 + 30*(car.capacity+1.2)
    return velocity
print (controlled_velocity(myambulance))
