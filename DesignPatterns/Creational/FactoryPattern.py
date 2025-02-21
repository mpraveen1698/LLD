


from abc import ABC, abstractmethod

#interface 
class Product(ABC):
    @abstractmethod
    def create(self):
        pass

#concrete methods
class Phone(Product):
    def create(self):
        print("Phone Created")

class Laptop(Product):
    def create(self):
        print("laptop created")


#Factory 

class ProductFactory:
    def createProduct(self, productType):
        if productType=="phone":
            return Phone()
        if productType=="laptop":
            return Laptop()

if __name__=="__main__":

    #client code
    PF=ProductFactory()
    phone=PF.createProduct("phone")
    phone.create()

    laptop=PF.createProduct("laptop")
    laptop.create()

        