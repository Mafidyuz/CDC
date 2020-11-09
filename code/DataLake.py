class DataLake:
    
    def __init__(self, ...): raise toImplement
    
    @abstractmethod
    def getCredential(self, configObj):
        raise notImplementedError
        
    @abstractmethod
    def _getconnectionobj(self, credential):
        raise notImplementedError
    
    def getConnectionObj(self, configObj):
        credential = self.getCredential(configObj)
        self._dl = self._getconnectionobj(credential)
        
    @abstractmethod
    def connect():
        raise notImplementedError

    @abstractmethod
    def insert(self):
        raise notImplementedError

