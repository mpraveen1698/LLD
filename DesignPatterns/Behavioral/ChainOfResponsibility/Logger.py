
from abc import ABC,abstractmethod

#this is abstract class that holds the chain of responsibility functionality
class LoggerHandler(ABC):
    def __init__(self, nextLogger):
        self.nextLogger=nextLogger  

    def log(self,loglevel, logmessage):
        if self.nextLogger:
            self.nextLogger.log(loglevel, logmessage)
        else:
            print("check the logging level "+ loglevel+ " is not avaliable")

class InfoLogger(LoggerHandler):
    def __init__(self,nextLogger):
        super().__init__(nextLogger)

    def log(self, loglevel,logmessage):
        if loglevel=='info':
            print("Logging info", logmessage)
        else:
            super().log(loglevel,logmessage)

class DebugLogger(LoggerHandler):
    def __init__(self,nextLogger):
        super().__init__(nextLogger)

    def log(self, loglevel,logmessage):
        if loglevel=='debug':
            print("Logging debug", logmessage)
        else:
            super().log(loglevel,logmessage)

class ErrorLogger(LoggerHandler):
    def __init__(self,nextLogger):
        super().__init__(nextLogger)

    def log(self, loglevel,logmessage):
        if loglevel=='error':
            print("Logging error", logmessage)
        else:
            super().log(loglevel,logmessage)

if __name__=="__main__":

    #this is client  which has a LoggingHandler 
    Logger=InfoLogger(DebugLogger(ErrorLogger(None)))
    Logger.log("info","Script Execution has started")
    Logger.log("debug","debug statement 1")
    Logger.log("debug","debug statement 2")
    Logger.log("error","Error encountered at line 3")
    Logger.log("warning","Error encountered at line 3")
    Logger.log("info","Script Execution has ended")



    




