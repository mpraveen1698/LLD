"""
Requirements:
Parking lot :
-->It should have multiple levels  with different number of spots
-->Parking lot will support different type of vechiles
--> each spot should support specific vechile
--> System should fill the spot when the vehicle is entering the lot and should release the spot when exited
--> System should track the spots and show the avaliablitu o
--> Lot should have multiple entry and exits
"""
from abc import ABC
from enum import Enum
from typing import List
###enum for vehicle type

class VehicleType(Enum):
    CAR =1
    TRUCK=2
    MOTORBIKE=3
##############################
class Vehicle(ABC):
    def __init__(self,LicenceNumber:str,vehicleType: VehicleType):
        self.LicenceNumber=LicenceNumber
        self.vehicleType=vehicleType
    
    def getVehicleType(self):
        return self.vehicleType
###create multiple vechile classes

class MotorCycle(Vehicle):
    def __init__(self, LicenceNumber):
        super().__init__(LicenceNumber, VehicleType.MOTORBIKE)
class Truck(Vehicle):
    def __init__(self,LicenceNumber):
        super().__init__(LicenceNumber,VehicleType.TRUCK)
class Car(Vehicle):
    def __init__(self, LicenceNumber):
        super().__init__(LicenceNumber, VehicleType.CAR)
###############################################

class ParkingSpot:
    def __init__(self, parkingSpotId:int,parkVehicleType: str):
        self.spotId=parkingSpotId
        self.vehicleType=parkVehicleType
        self.parkedVehicle=None  #vehicle object
    
    def isAvaliable(self):
        return True if self.parkedVehicle == None else False
    
    def parkVehicle(self,VehicleEnter):
        if self.isAvaliable() and self.vehicleType==VehicleEnter.getVehicleType():
            self.parkedVehicle=VehicleEnter
        else:
            raise Exception("Spot is not Avaliable or MisMatch with Vehicle Type")
    def unParkVechile(self):
        self.parkedVehicle=None
    
    def getSpotId(self):
        return self.spotId

    def getVehicleType(self):
        return self.vehicleType
    
    def getParkedVehicle(self):
        return self.parkedVehicle

#############################
class Level:
    def __init__(self,levelNo : int , ListOfSpots:List[ParkingSpot]):
        self.level=levelNo
        self.parking_spots: List[ParkingSpot]=ListOfSpots
    
    def parkVehicleInLevel(self,Vehicle):
        for parkingspot in self.parking_spots:
            if parkingspot.isAvaliable() and parkingspot.getVehicleType()==Vehicle.getVehicleType():
                parkingspot.parkVehicle(Vehicle)
                return True
        return False

    def unParkVehicleLevel(self,Vehicle):
        for parkingspot in self.parking_spots:
            if not parkingspot.isAvaliable() and parkingspot.getParkedVehicle()==Vehicle:
                parkingspot.unParkVechile()
                return True
        return False
    
    def displayAvaliability(self):
        for spot in self.parking_spots:
            print(f"Spot {spot.getSpotId()}: {'Available' if spot.isAvaliable() else 'Occupied'}")


class ParkingLot:
    instance_=None
    def __new__(cls):
        if cls.instance_==None:
            cls.instance_=super().__new__(cls)
            cls.instance_.levels=[]
        return cls.instance_

 
    def addLevel(self,level):
        self.levels.append(level)
    
    def parkVehicle(self,vehicle):
        for level in self.levels:
            if level.parkVehicleInLevel(vehicle):
                return True
        return False

    def unParkVehicle(self,vehicle):
        for level in self.levels:
            if level.unParkVehicleLevel(vehicle):
                return True
        return False
    def displayAvaliablity(self):
        for level in self.levels:
            print(level.level)
            level.displayAvaliability()


class Entrance:
    def __init__(self,entranceid:int, parkinglot: ParkingLot):
        self.enterId=entranceid
        self.parkinglot=parkinglot

    def entry(self,vehicle:Vehicle):
        self.ParkingLot.parkVehicle(vehicle)

class Exit:
    def __init__(self,exitID:int, parkinglot: ParkingLot):
        self.exitID=exitID
        self.parkinglot=parkinglot

    def exit(self,vehicle:Vehicle):
        self,ParkingLot.unParkVehicle(vehicle)


###########
PL=ParkingLot()
listOfParkingSpots=[ParkingSpot(1,VehicleType.CAR),
                    ParkingSpot(2,VehicleType.TRUCK),
                    ParkingSpot(3,VehicleType.MOTORBIKE),
                    ParkingSpot(4,VehicleType.CAR),
                    ParkingSpot(5,VehicleType.TRUCK)
                    ]

level1=Level(1,listOfParkingSpots)


PL.addLevel(level1)


Car1=Car("XYZ123")
Car2=Car("YYYY345")

M1=MotorCycle("hruhgir")
T1=Truck("oriht")

PL.parkVehicle(Car1)
PL.displayAvaliablity()
PL.parkVehicle(Car2)
PL.displayAvaliablity()
PL.unParkVehicle(Car1)
PL.parkVehicle(M1)
PL.displayAvaliablity()


#optimizations
#need to work on more things like multiple entrances ..
#singleton implementation  for parkinglot, implemented using __new__(cls)




    
    
