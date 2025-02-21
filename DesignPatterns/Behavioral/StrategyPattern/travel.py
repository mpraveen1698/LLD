# Here, the Strategy Pattern works like this:

# Context: You (the traveler).
# Strategy: The travel method (Car, Train, or Plane).
# Concrete Strategies: The specific implementations of traveling by Car, Train, or Plane.


from abc import ABC, abstractmethod
#Strategy
class TravelStrategy(ABC):
    @abstractmethod
    def travel(self):
        pass

#concrete Strategies

class Car(TravelStrategy):
    def travel(self):
        print("Travelling by Car")

class Train(TravelStrategy):
    def travel(self):
        print("Travelling by Train")

class Plane(TravelStrategy):
    def travel(self):
        print("Travelling by Plane")


#context is traveller 

class Traveller:
    def __init__(self, TravelStrategy):
        self.TravelStrategy=TravelStrategy
    def set_strategy(self,TravelStrategy):
        self.TravelStrategy=TravelStrategy
    
    def transport(self):
        self.TravelStrategy.travel()

if __name__=='__main__':
    Me=Traveller(Train()) #initially planned to travel by Train 
    Me.transport()

#switch to car 
    Me.set_strategy(Car())
    Me.transport()

    #switch to plane
    Me.set_strategy(Plane())
    Me.transport()



