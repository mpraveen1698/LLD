from abc import ABC, abstractmethod

#interface 
class Product(ABC):
    def __init__(self,company):
        self.company=company
    @abstractmethod
    def create(self):
        pass

#create concrete class

class Mobile(Product):
    def create(self):
        print(self.company+" Mobile created....")

class Laptop(Product):
    def create(self):
        print(self.company+" Laptop created....")


#interface for company 

class ProductCompany(ABC):
    @abstractmethod
    def createProduct(self,ProductName):
        pass

#create concreate class

class AppleCompany(ProductCompany):
    def __init__(self):
        self.company="apple"

    def createProduct(self,ProductName):
        if ProductName=='mobile':
            return Mobile(self.company)
        if ProductName=='laptop':
            return Laptop(self.company)

class SamsungCompany(ProductCompany):
    def __init__(self):
        self.company="samsung"
    def createProduct(self,ProductName):
        if ProductName=='mobile':
            return Mobile(self.company)
        if ProductName=='laptop':
            return Laptop(self.company)

#createfacrory 

class ProductFactory:
    def selectCompany(self, companyName):
        if companyName=="apple":
            return AppleCompany()
        if companyName=="samsung":
            return SamsungCompany()
    

if __name__=="__main__":
    #client 
    PF=ProductFactory()
    company=PF.selectCompany('apple')
    mobile=company.createProduct('mobile')
    mobile.create()
    mobile=company.createProduct('laptop')
    mobile.create()

    company=PF.selectCompany('samsung')
    mobile=company.createProduct('mobile')
    mobile.create()
    mobile=company.createProduct('laptop')
    mobile.create()



        

    