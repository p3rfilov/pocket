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
        item = self.ui.list_items.currentItem()
        widget = self.ui.list_items.itemWidget(item)
        widget.toggleWidgetTextField()
        item.setSizeHint(widget.sizeHint())
        
    def closeInactiveItems(self):
        count = self.ui.list_items.count()
        for row in range(count):
            if row != self.ui.list_items.currentRow():
                item = self.ui.list_items.item(row)
                widget = self.ui.list_items.itemWidget(item)
                widget.toggleWidgetTextField(setHidden=True)
                item.setSizeHint(widget.sizeHint())
    
    def removeRow(self):
        row = self.ui.list_items.currentRow()
        self.ui.list_items.takeItem(row)
              

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())
            