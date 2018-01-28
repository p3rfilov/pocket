import os
import sqlite3
from collections import namedtuple

class dataStore():
    '''This class provides the data storage and retrieval interface.'''
    def __init__(self, location, fields):
        self.location = str(location)
        self.fields = fields
        self.connection = None
        self.cursor = None
        
        if os.path.exists(self.location):
            self.getAllData()
        else:
            self.createNewDB()
    
    def createNewDB(self):
        self.connect()
        self.execute( "CREATE TABLE Pockets ({f} TEXT NOT NULL UNIQUE)"\
                      .format(f=self.fields[0]) )
        for field in self.fields[1:]:
            self.execute( "ALTER TABLE Pockets ADD COLUMN {f} TEXT"\
                          .format(f=field) )

    def connect(self):
        self.connection = sqlite3.connect(self.location)
        self.connection.isolation_level = None # auto-commit mode
        self.cursor = self.connection.cursor()
        
    def disconnect(self):
        self.connection.close()

    def execute(self, command):
        self.cursor.execute(command)

    def createRecord(self, name):
        try:
            self.execute( "INSERT INTO Pockets ({f}) VALUES ('{n}')"\
                          .format(f=self.fields[0], n=name) )
            return True
        except:
            print('Name already exists!')
            return False
    
    def deleteRecord(self, name):
        try:
            
            self.execute("DELETE FROM Pockets WHERE {f} = '{n}'"\
                         .format(f=self.fields[0], n=name) )
            return True
        except:
            print('Could not delete record!')
            return False
    
    def readFrom(self, name):
        pass
    
    def writeTo(self, name):
        pass
        
    def getAllData(self):
        self.connect()
        self.execute("SELECT * FROM Pockets")
        data = self.cursor.fetchall()
        packedData = [dict(zip(self.fields, pocket)) for pocket in data]
        return packedData
        