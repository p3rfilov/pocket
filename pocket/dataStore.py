import os
import sqlite3
from collections import namedtuple

class dataStore():
    '''This class provides the data storage and retrieval interface.'''
    def __init__(self, location, columns):
        self.location = str(location)
        self.columns = columns
        self.currentRecord = None
        
        if self.locationExists():
            self.getAllData()
        else: self.createNew()
    
    def locationExists(self):
        return os.path.exists(self.location)
    
    def createNew(self):
        if True:
            pass
        else:
            print('Could not create database at ' + self.location)
            self.location = None
    
    def setCurrentRecord(self, name):
        if name in self.columns:
            self.currentRecord = name
        else:
            self.currentRecord = None
            print('No such record found!')
    
    def readFrom(self, column):
        if self.currentRecord:
            pass
    
    def writeTo(self, column):
        if self.currentRecord:
            pass
        
    def getAllData(self):
        pass