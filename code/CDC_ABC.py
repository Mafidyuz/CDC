from abc import ABC, abstractmethod

class CDC_ABC(ABC):
    
    def __init__(self):
        self.datalake = Datalake(...)
        
    @abstractmethod
    def createSyncFile():
        raise notImplementedError
    
    @abstractmethod   
    def getFreshData(self):
        raise notImplementedError
        
    @abstractmethod
    def insertIntoDatalake(operation, row):
        raise notImplementedError
        
    def insertEvent(row):
        insertIntoDataLake("INSERT", row)
        
    def updateEvent(row):
        insertIntoDataLake("UPDATE", row)
        
    def deleteEvent(row):
        insertIntoDataLake("DELETE", row)

