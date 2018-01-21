import os
from ui_dataWidget import dataWidget
from ui_mainWindow import mainWindow
from dataStore import dataStore

class Settings():
    appName = 'pocket'
    root = os.getenv('APPDATA')
    location = root + ''
    columns = ('title','data')

class pocket_main():
    def __init__(self):
        self.window = mainWindow()
        self.window.ui.btn_addPocket.clicked.connect(self.addNewPocket)
        self.window.ui.search.textChanged.connect(self.searchText)
        
        self.dataStore = dataStore(Settings.location, Settings.columns)
        self.allData = self.dataStore.getAllData()
        
    def addNewPocket(self):
        widget = dataWidget()
#         widget.setTitle(params['title'])
#         widget.setData(params['data'])
        widget.delButton.clicked.connect(self.deletePocketInquiry)
        widget.editButton.clicked.connect(self.beginEditSession)
        widget.cancelButton.clicked.connect(self.endEditSession)
        self.window.addNewRow(widget)
        
    def deletePocketInquiry(self):
        if True:
            self.window.removeCurrentRow()
            
    def beginEditSession(self):
        widget = self.window.getCurrentWidget()
        widget.setEditState(True)
        
    def endEditSession(self):
        widget = self.window.getCurrentWidget()
        widget.setEditState(False)
        
    def searchText(self):
        pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)       
    pocket = pocket_main()
    sys.exit(app.exec_())