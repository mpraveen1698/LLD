#first we need to define the base interface (coffeeBase Interface)

#We have to create the decorater such that it will add functionality to the  base (coffeeAddOn Inferace  like  sugar , creamer etc..
#)


# Base Interface

from abc import ABC , abstractmethod

class BaseCoffee(ABC):
    @abstractmethod
    def cost(self):
        pass


#decorater 

class CoffeeDecorater(BaseCoffee):
    def __init__(self, baseCoffeeObj:BaseCoffee):
        self.baseCoffeeObj=baseCoffeeObj
    def cost(self):
        return self.baseCoffeeObj.cost()


#concrete implementation

#let say we have different types of coffee's

class CappuccinoCoffee(BaseCoffee):

    def cost(self):
        return 100

class ExpressoCoffee(BaseCoffee):

    def cost(self):
        return 110


#let define some addon's for the coffee

class SugarAddon(CoffeeDecorater):
    
    def cost(self):
        return self.baseCoffeeObj.cost()+10

class CreamerAddon(CoffeeDecorater):
    def cost(self):
        return self.baseCoffeeObj.cost()+15


if __name__=="__main__":
    coffee=CappuccinoCoffee()
    print("Base capachino", coffee.cost())

    #add sugar 
    
    sugarcoffee=SugarAddon(coffee)
    print("Base capachino + sugar", sugarcoffee.cost())

    #add creamer to the base +sugar 

    creamercoffee=CreamerAddon(sugarcoffee)
    print("Base capachino + sugar+ creamer", creamercoffee.cost())
    
    