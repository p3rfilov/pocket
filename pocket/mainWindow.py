from PyQt5.QtWidgets import QMainWindow, QListWidgetItem
from PyQt5.uic import loadUi
from dataWidget import dataWidget

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi('mainWindow.ui')
        self.ui.show()
        
        for i in range(5):
            itemData =  {
                        'title':'Item ' + str(i),
                        'expanded':'False',
                        'data':str(i)*30
                        }
            
            self.widget = dataWidget(itemData)
            self.listItem = QListWidgetItem()
            self.listItem.setSizeHint(self.widget.sizeHint())
            self.ui.list_items.addItem(self.listItem)
            self.ui.list_items.setItemWidget(self.listItem, self.widget)
            
            