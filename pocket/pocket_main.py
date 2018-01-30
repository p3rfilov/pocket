import os
from ui_dataWidget import dataWidget
from ui_mainWindow import mainWindow
from dataStore import dataStore

class Settings():
    appName = 'pocket'
    root = os.getenv('APPDATA') + '\\pocket'
    location = root + '\\pocket.db'
    fields = ('name','data')
    appIni = root + '\\pocket.ini'

class pocket_main():
    def __init__(self):
        self.tempData = None
        
        self.window = mainWindow()
        self.window.ui.btn_addPocket.clicked.connect(self.addNewPocket)
        self.window.ui.newName.returnPressed.connect(self.addNewPocket)
        self.window.ui.search.textChanged.connect(self.searchText)
        
        self.checkAndPopulateAppFolder()
        self.dataStore = dataStore(Settings.location, Settings.fields)
        self.pullAllPockets()
    
    def pullAllPockets(self):
        allData = self.dataStore.getAllData()
        for data in allData:
            self.addPocket(data)
    
    def checkAndPopulateAppFolder(self):
        if not os.path.exists(Settings.root):
            os.makedirs(Settings.root)
        f = open(Settings.appIni, 'a')
        f.close()
    
    def addNewPocket(self):
        name = self.window.getNewNameText()
        if name:
            result = self.dataStore.createRecord(name)
            if result:
                self.addPocket({'name':name,'data':None})
                self.window.clearNewNameText()
                self.window.expandCurrentItem()
                self.beginEditSession()
        
    def addPocket(self, params):
        widget = dataWidget()
        widget.setName(params['name'])
        widget.setNotes(params['data'])
        widget.delButton.clicked.connect(self.deletePocket)
        widget.editButton.clicked.connect(self.beginEditSession)
        widget.cancelButton.clicked.connect(self.endEditSession)
        widget.okButton.clicked.connect(lambda: self.endEditSession(commit=True))
        self.window.addNewRow(widget)
        
    def deletePocket(self):
        name = self.window.getCurrentWidget().getName()
        if self.dataStore.deleteRecord(name):
            self.window.removeCurrentRow()
            
    def beginEditSession(self):
        self.tempData = self.window.getCurrentWidget().getNotes()
        self.window.getCurrentWidget().setEditState(True)
        
    def endEditSession(self, commit=False):
        if commit:
            name = self.window.getCurrentWidget().getName()
            notes = self.window.getCurrentWidget().getNotes()
            data = self.dataStore.packData((name,notes))
            self.dataStore.write(data)
        else:
            self.window.getCurrentWidget().setNotes(self.tempData)
        self.window.getCurrentWidget().setEditState(False)
        
    def searchText(self):
        pass
    
    def saveRowOrder(self):
        pass
    
    def loadRowOrder(self):
        pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)       
    pocket = pocket_main()
    sys.exit(app.exec_())