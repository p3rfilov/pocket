import os
import atexit
from components.ui_dataWidget import dataWidget
from components.ui_mainWindow import mainWindow
from components.ui_Message import Message
from components.dataStore import dataStore

class Settings():
    appName = 'pocket'
    root = os.getenv('APPDATA') + '\\pocket'
    location = root + '\\pocket.db'
    fields = ('name','data')
    rowOrder = root + '\\rowOrder.ini'

class pocket_main():
    def __init__(self):
        self.tempData = None
        self.matchedRows = []
        
        self.window = mainWindow()
        self.window.ui.btn_addPocket.clicked.connect(self.addNewPocket)
        self.window.ui.newName.returnPressed.connect(self.addNewPocket)
        self.window.ui.search.textChanged.connect(self.searchText)
        self.window.ui.btn_searchNext.clicked.connect(self.searchNext)
        self.window.ui.btn_searchPrev.clicked.connect(self.searchPrev)
        self.enableArrows(False)
        
        self.checkAndPopulateAppFolder()
        self.dataStore = dataStore(Settings.location, Settings.fields)
        self.pullAllPockets()
        
        # save row order on exit
        atexit.register(self.saveRowOrder)
    
    def pullAllPockets(self):
        allData = self.dataStore.getAllData()
        orderedRows = self.getRowOrder()
        passed = self.integrityCheck(allData, orderedRows)
        if passed:
            for row in orderedRows:
                rowData = [d for d in allData if d['name'] == row][0]
                self.addPocket(rowData)
        else: 
            for data in allData: self.addPocket(data)
            Message().rowOrderFail()
    
    def integrityCheck(self, data, names):
        if len(data) == len(names):
            if sorted([d['name'] for d in data]) == sorted(names):
                return True
            else: return False
        else: return False
    
    def checkAndPopulateAppFolder(self):
        if not os.path.exists(Settings.root):
            os.makedirs(Settings.root)
        f = open(Settings.rowOrder, 'a')
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
                self.saveRowOrder()
            else:
                Message().duplicateRecord()
        
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
        if Message().delete():
            name = self.window.getCurrentWidget().getName()
            if self.dataStore.deleteRecord(name):
                self.window.removeCurrentRow()
                self.saveRowOrder()
            
    def beginEditSession(self):
        self.tempData = self.window.getCurrentWidget().getNotes()
        self.window.getCurrentWidget().setEditState(True)
        
    def endEditSession(self, commit=False):
        if commit:
            name = self.window.getCurrentWidget().getName()
            notes = self.window.getCurrentWidget().getNotes()
            self.dataStore.write((name,notes))
        else:
            self.window.getCurrentWidget().setNotes(self.tempData)
        self.window.getCurrentWidget().setEditState(False)

    def searchText(self):
        self.matchedRows = []
        self.enableArrows(False)
        self.window.closeInactiveItems(closeAll=True)
        self.findMatchedRows()
                
        if not self.window.ui.search.text():
            self.matchedRows = []
        
        if self.matchedRows:
            self.enableArrows(True)
            first = self.matchedRows[0]
            self.setRowAndExpand(first)
            
    def findMatchedRows(self):
        for row in range(self.window.getRowCount()):
            item = self.window.getItem(row)
            widget = self.window.getItemWidget(item)
            name = widget.getName()
            notes = widget.getNotes()
            if not self.window.ui.search.text() in name + notes:
                item.setHidden(True)
            else:
                item.setHidden(False)
                self.matchedRows.append(row)
            
    def enableArrows(self, state):
        self.window.ui.btn_searchPrev.setEnabled(state)
        self.window.ui.btn_searchNext.setEnabled(state)
        
    def setRowAndExpand(self, row):
        self.window.setCurrentRow(row)
        self.window.expandCurrentItem(toggleMode=False)
                
    def searchNext(self):
        self.window.closeInactiveItems(closeAll=True)
        currentIndex = self.matchedRows.index(self.window.getCurrentRow())
        nextIndex = currentIndex + 1
        if (nextIndex + 1) <= len(self.matchedRows):
            row = self.matchedRows[nextIndex]
            self.setRowAndExpand(row)
        else:
            row = self.matchedRows[0]
            self.setRowAndExpand(row)
    
    def searchPrev(self):
        self.window.closeInactiveItems(closeAll=True)
        currentIndex = self.matchedRows.index(self.window.getCurrentRow())
        prevIndex = currentIndex - 1
        if prevIndex >= 0:
            row = self.matchedRows[prevIndex]
            self.setRowAndExpand(row)
        else:
            row = self.matchedRows[len(self.matchedRows) - 1]
            self.setRowAndExpand(row)

    def saveRowOrder(self):
        rowList = []
        for row in range(self.window.getRowCount()):
            item = self.window.getItem(row)
            widget = self.window.getItemWidget(item)
            name = widget.getName()
            rowList.append(name)
        
        with open(Settings.rowOrder, 'w') as file:
            file.write('<pocketItem>'.join(rowList))
    
    def getRowOrder(self):
        with open(Settings.rowOrder, 'r') as file:
            return list(reversed(file.read().split('<pocketItem>')))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)       
    pocket = pocket_main()
    sys.exit(app.exec_())