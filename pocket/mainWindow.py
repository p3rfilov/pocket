import os
import sys
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QListWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from dataWidget import dataWidget

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uiDir = os.path.dirname(__file__)
        uiFile = os.path.join(uiDir, 'mainWindow.ui')
        self.ui = loadUi(uiFile)
        self.ui.show()
        
        self.ui.list_items.setSizeAdjustPolicy(QListWidget.AdjustToContents)
        self.ui.list_items.itemClicked.connect(self.expandCurrentItem)
        
    def addNewPocket(self, params):
        widget = dataWidget()
        widget.setTitle(params['name'])
        widget.setData(params['data'])
        listItem = QListWidgetItem()
        listItem.setSizeHint(widget.sizeHint())
        self.ui.list_items.addItem(listItem)
        self.ui.list_items.setItemWidget(listItem, widget)
        
        widget.delButton.clicked.connect(self.removeRow)
        widget.editButton.clicked.connect(lambda: widget.setEditState(True))
        widget.cancelButton.clicked.connect(lambda: widget.setEditState(False))
        
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
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())
            