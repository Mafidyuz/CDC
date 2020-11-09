from hashlib import sha256

class CDC(CDC_ABC):
    
    def __init__(self, app_name, processId, filename, khashfun=sha256, hashfun=sha256):
        super.__init__(self, ...)
        self.app_name = app_name
        self.processId = processId
        self.lastSyncJson = SyncFile()
        self.khashfun = khashfun
        self.hashfun = hashfun
        

    def setUpHashValues(self):
        data = {}
        for row in db:
            data[self.getKeyHash(row)] = self.getValueHash(row)
        return data


    def getKeyHash(self, row):
        m = self.khashfun
        for value in row:
            m.update(str(value))
        return m.digest()
            
    def getValueHash(self, row):
        m = self.hashfun
        for value in row:
            m.update(str(value))
        return m.digest()

    def getFreshData(self):
        keys = []
        data = self.lastSyncJson.getDict()
        
        for row in db:
            key = self.getKeyHash(row) 
            khash = self.getValueHash(row)
            self.lastSyncJson.append(key, khash)
            keys.append[key]
            if key not in data:
                self.insert(row)
            if data[key] != khash:
                self.update(row)
        
        for key in data.keys - keys: #Fare bene
            self.delete(...)
        
        #No need to update lastSyncJson couse it is updated incrementally...

"""
    def getFreshData(self):
        newData = setUpHashValues()
        for key in set(self.data + newData):
            if key not in newData:
                self.logtable.delete(...)
            elif key not in self.data:
                self.logtable.insert(...)
            elif(self.data[key] != newData[key]):
                self.logtable.update(...)
        self.data = newData 
"""

    def connectToDataSource(): pass
    
    def connectToDataLake():
        raise notImplementedError
        
    def createSyncFile():
        self.data = self.setUpHashValues()
        
    def insertIntoDatalake(operation, row):
        #write su un file
        raise notImplementedError

