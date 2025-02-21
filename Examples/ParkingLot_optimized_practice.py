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


from enum import Enum 
class VehicleType(Enum):
    CAR=1
    MOTORCYCLE=2
    TRUCK=3

class Vehicle:
    def __init__(self, Number, typeOfVechile):
        self.vehicleNumber=Number
        self.vehicleType=typeOfVechile

    def getVehicleType(self):
        return self.vehicleType
#Vehicle Types

class Car(Vehicle):
    def __init__(self, Number):
        super().__init__(Number, VehicleType.CAR)

class MotorCycle(Vehicle):
    def __init__(self, Number):
        super().__init__(Number, VehicleType.MOTORCYCLE)

class Truck(Vehicle):
    def __init__(self, Number):
        super().__init__(Number, VehicleType.TRUCK)

## Parking Spot

class ParkingSpot:
    def __init__(self, parkingID,typeofVehicle:str):
        self.parkingID=parkingID
        self.typeOfVehicle=typeofVehicle
        self.vehicleParked= None

    def isAvaliable(self):
        return True if self.vehicleParked==None else False
    
    def unParkVehicle(self):
        self.vehicleParked=None

    def parkVehicle(self,vehicle):
        self.vehicleParked=vehicle
    
    def getParkingID(self):
        return self.parkingID
    
    def getTypeOfVehicle(self):
        return self.typeOfVehicle
    
    def getVehicleParked(self):
        return self.vehicleParked
 
class Level:
    def __init__(self, levelNo, parkingSpots):
        self.levelNo=levelNo
        self.parkingSpots=parkingSpots
    
    def displayAvaliablity(self):
        for parkingSpot in self.parkingSpots:
            print(parkingSpot.parkingID , "Avaliable" if parkingSpot.isAvaliable() else "Occupied")
    
class ParkingLot:
    _instance=None
    def __new__(cls):
        if cls._instance is None :
            cls._instance=super().__new__(cls)
            cls._instance.levels=[]
            cls._instance.availableSpots={
                VehicleType.CAR:set(),
                VehicleType.MOTORCYCLE:set(),
                VehicleType.TRUCK:set()
            }
        return cls._instance

    def addLevel(self,level):
        self.levels.append(level)
        for spot in level.parkingSpots:
            self.availableSpots[spot.getTypeOfVehicle()].add(spot)
    
    def parkVehicle(self,newVehicle):
        # for level in self.levels:
        #     if level.parkVehicle(newVehicle):
        #         return True
        # return False
        if not self.availableSpots[newVehicle.getVehicleType()]:
            return False
        spot=self.availableSpots[newVehicle.getVehicleType()].pop()
        spot.parkVehicle(newVehicle)
        return True
    
        
    def unParkVehicle(self,vehicle):
        # for level in self.levels:
        #     if level.unParkVehicle(vehicle):
        #         return True
        # return False
        for level in self.levels:
            for spot in level.parkingSpots:
                if spot.getVehicleParked()==vehicle:
                    spot.unParkVehicle()
                    self.availableSpots[vehicle.getVehicleType()].add(spot)
                    return True
        return False
    
    def displayAvaliablity(self):
        for  level in self.levels:
            print('level')
            level.displayAvaliablity()

class Entry:
    def __init__(self,id,parkingLot):
        self.entryId=id
        self.parkingLot=parkingLot
    def enter(self,newVehicle):
        self.parkingLot.parkVehicle(newVehicle)

class Exit:
    def __init__(self,id,parkingLot):
        self.exitId=id
        self.parkingLot=parkingLot
    
    def exit(self,vehicle):
        self.parkingLot.unParkVehicle(vehicle)


if __name__=="__main__":
    parkingLot=ParkingLot()

    level=Level(1,[ParkingSpot(1,VehicleType.CAR),
                    ParkingSpot(2,VehicleType.TRUCK),
    ParkingSpot(3,VehicleType.CAR),
    ParkingSpot(4,VehicleType.MOTORCYCLE),
    ParkingSpot(5,VehicleType.TRUCK)])

    parkingLot.addLevel(level)

    car1=Car("12324")
    car2=Car("1236824")

    bike=MotorCycle("584574")
    truck=Truck("57843")

    entry1=Entry(1,parkingLot)
    entry2=Entry(2,parkingLot)
    exit1=Exit(1,parkingLot)
    exit2=Exit(2,parkingLot)
        
    
    entry1.enter(car1)
    entry1.enter(truck)
    parkingLot.displayAvaliablity()
    entry2.enter(car2)
    parkingLot.displayAvaliablity()
    exit1.exit(car1)
    parkingLot.displayAvaliablity()
        

# ## optimizations

# #by adding distance at ParkingSpot , we add functionality of getting nearer spot avaliable using min heap then time complexity will O(log N)


# # can ADD The strategy pattern , can add dynamically  : FirstAvaliable spot, NearSpot , Random Spots 
# from abc import ABC, abstractmethod

# class ParkingStrategy(ABC):
#     @abstractmethod
#     def findSpot(self, available_spots, vehicle_type):
#         pass

# class FirstAvailableStrategy(ParkingStrategy):
#     def findSpot(self, available_spots, vehicle_type):
#         return available_spots[vehicle_type].pop() if available_spots[vehicle_type] else None




# can add billings or Payment 
# adding certain levels to the entries 
#can add vehicle registary, where we can add the different type of vehicles dynamically , now as we assigned hardcoded values using Enum ,it violates open/close principle


