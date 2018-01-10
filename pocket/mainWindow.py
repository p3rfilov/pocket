from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QListWidget
from PyQt5.uic import loadUi
from dataWidget import dataWidget

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi('mainWindow.ui')
        self.ui.show()
        
        self.ui.list_items.setSizeAdjustPolicy(QListWidget.AdjustToContents)
        self.ui.list_items.itemClicked.connect(self.expandCurrentItem)
        
        for i in range(5):
            listItem = QListWidgetItem()
            widget = dataWidget()
            widget.setTitle('Note ' + str(i))
            widget.setData(str(i)*10)
            listItem.setSizeHint(widget.sizeHint())
            self.ui.list_items.addItem(listItem)
            self.ui.list_items.setItemWidget(listItem, widget)
            
            widget.delButton.clicked.connect(self.removeRow)
            
        
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
              
        
            
            