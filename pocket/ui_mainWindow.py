import os
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QListWidget
from PyQt5.uic import loadUi

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uiDir = os.path.dirname(__file__)
        uiFile = os.path.join(uiDir, 'ui_mainWindow.ui')
        self.ui = loadUi(uiFile)
        self.ui.show()
        
        self.ui.list_items.setSizeAdjustPolicy(QListWidget.AdjustToContents)
        self.ui.list_items.itemClicked.connect(self.expandCurrentItem)
        
    def addNewRow(self, widget):
        listItem = QListWidgetItem()
        listItem.setSizeHint(widget.sizeHint())
        self.ui.list_items.addItem(listItem)
        self.ui.list_items.setItemWidget(listItem, widget)
        
    def expandCurrentItem(self):
        self.closeInactiveItems()
        item = self.getCurrentItem()
        widget = self.getItemWidget(item)
        widget.toggleWidgetTextField()
        item.setSizeHint(widget.sizeHint())
        
    def closeInactiveItems(self):
        count = self.getRowCount()
        for row in range(count):
            if row != self.getCurrentRow():
                item = self.getItem(row)
                widget = self.getItemWidget(item)
                widget.toggleWidgetTextField(setHidden=True)
                item.setSizeHint(widget.sizeHint())
    
    def getCurrentWidget(self):
        item = self.getCurrentItem()
        widget = self.getItemWidget(item)
        return widget
                
    def getRowCount(self):
        return self.ui.list_items.count()
    
    def getCurrentRow(self):
        return self.ui.list_items.currentRow()
    
    def getCurrentItem(self):
        return self.ui.list_items.currentItem()
    
    def getItem(self, row):
        return self.ui.list_items.item(row)
    
    def getItemWidget(self, item):
        return self.ui.list_items.itemWidget(item)
    
    def removeCurrentRow(self):
        row = self.getCurrentRow()
        self.ui.list_items.takeItem(row)
              

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())
            