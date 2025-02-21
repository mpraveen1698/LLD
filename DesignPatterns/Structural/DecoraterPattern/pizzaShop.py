#Base Pizza

from abc import ABC,abstractmethod


class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass


#wrapper or decorater around the BasePizza 

class PizzaAddOn(BasePizza):

    def __init__(self, basepizza : BasePizza):
        self.basepizza=basepizza
    
    def cost(self):
        return self.basepizza.cost()
    

#creating different type pizza's

class VegPizza(BasePizza):
    def cost(self):
        return 100

class NonVegPizza(BasePizza):
    def cost(self):
        return 110


#creating different types of decoraters

class Onions(PizzaAddOn):
    def cost(self):
        return self.basepizza.cost()+5

class Cheese(PizzaAddOn):
    def cost(self):
        return self.basepizza.cost()+10

class AllVeggies(PizzaAddOn):
    def cost(self):
        return self.basepizza.cost()+12

if __name__=="__main__":

    #creating base pizza  (veg type)

    vegpizza=VegPizza()
    print('cost of base veg', vegpizza.cost())

    #add onions
    onionpizza=Onions(vegpizza)
    print('base veg +onion', onionpizza.cost())

    #add cheese
    cheesepizza=Cheese(onionpizza)
    print('base veg +onion+cheese', cheesepizza.cost())

    #add veggies
    allvegiespizza=AllVeggies(cheesepizza)
    print('base veg +onion+cheese+veggies', allvegiespizza.cost())

    #add cheese
    finalpizza=Cheese(allvegiespizza)
    print('base veg +onion+cheese+veggies+cheese', finalpizza.cost())


