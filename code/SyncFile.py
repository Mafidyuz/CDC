import json

class SyncFile:
    
    def __init__(self, path, filename):
        self.file = open(path+filename, 'w')
        
    def insert(self, data):
        self.file.write(data)
        
    def getDict(self):
        return json.load(path+filename) #trasformare in dict

