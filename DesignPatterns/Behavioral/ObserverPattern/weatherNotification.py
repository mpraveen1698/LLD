#we need to define oberservable(weatherOberservableInterface) and observer(DisplayInterfaces)
#In Observable:
#we need to define the logic for adding ,removing and notify the observer when ever there is an update in the data or state 
#it should have the list of observers

from abc import ABC, abstractmethod

#observable interface 
class Observerable(ABC):

    @abstractmethod
    def addObserver(self,DisplayObserver):
        pass
    @abstractmethod
    def removeObserver(self,DisplayObserver):
        pass
    @abstractmethod
    def notify(self):
        pass
    @abstractmethod
    def set_data(self,int):
        pass

    @abstractmethod
    def get_data(self):
        pass

#observer interface
class DisplayObserver(ABC):
    obj=None #observable obj
    def __init__(self, obj):
        self.obj=obj
    @abstractmethod
    def update(self):
        pass


#observable concerte implementation

class WeatherObservable(Observerable):
    def __init__(self):
        self.listofObservers=[]
        self.currTemp=0
    
    def addObserver(self,DO):
        self.listofObservers.append(DO)
    
    def removeObserver(self,DO):
         self.listofObservers.remove(DO)
    
    def notify(self):
        for obj in self.listofObservers:
            obj.update()
    
    def set_data(self,newTemp):
        if self.currTemp!=newTemp:
            self.currTemp=newTemp
            self.notify()

    def get_data(self):
        return self.currTemp

#Observer concrete implementation

class TVDisplay(DisplayObserver):
    def __init__(self,obj):
        super().__init__(obj)
    def update(self):
        print(self.obj.get_data() ,"Display in TV")

class WatchDisplay(DisplayObserver):
    def __init__(self,obj):
        super().__init__(obj)
    def update(self):
        print(self.obj.get_data() ,"Display in Watch")

class MobileDisplay(DisplayObserver):
    def __init__(self,obj):
        super().__init__(obj)
    def update(self):
        print(self.obj.get_data() ,"Display in Mobile")

if __name__ =='__main__':
    #creation of weather observable
    WO=WeatherObservable()
    #creating the observer's
    TVD=TVDisplay(WO)
    Watch=WatchDisplay(WO)
    MD=MobileDisplay(WO)

    #adding all observers to Observable
    WO.addObserver(TVD)
    WO.addObserver(Watch)
    WO.addObserver(MD)

    #initate the notification by change in data or state
    WO.set_data(10)
    WO.set_data(100)
    #now notification will not send as there is no change in data
    WO.set_data(100)

    #removing watch observer
    WO.removeObserver(Watch)
    WO.set_data(0)








