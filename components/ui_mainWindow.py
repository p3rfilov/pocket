import os
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QListWidget, QSystemTrayIcon, QAction, QMenu, qApp
from PyQt5 import QtCore
from PyQt5.uic import loadUi

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dir = os.path.dirname(__file__)
        self.ui = loadUi(os.path.join(self.dir, 'ui_mainWindow.ui'))
        self.ui.show()
        
        self.ui.list_items.setSizeAdjustPolicy(QListWidget.AdjustToContents)
        self.ui.list_items.itemClicked.connect(self.expandCurrentItem)
        
        # tray icon
        self.ui.closeEvent = self.minimizeToTray # minimize to Tray instead of closing
        
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.ui.windowIcon())
        self.tray_icon.setToolTip('pocket')
        
        quit_action = QAction("Exit", self)
        self.tray_icon.activated.connect(self.trayIconClick)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
    
    def minimizeToTray(self, event):
        event.ignore()
        self.ui.hide()
        
    def trayIconClick(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.ui.show()
        
    def addNewRow(self, widget):
        listItem = QListWidgetItem()
        listItem.setSizeHint(widget.sizeHint())
        self.ui.list_items.insertItem(0, listItem)
        self.setCurrentRow(0)
        self.ui.list_items.setItemWidget(listItem, widget)
        
    def expandCurrentItem(self, toggleMode=True):
        self.closeInactiveItems()
        item = self.getCurrentItem()
        widget = self.getItemWidget(item)
        if toggleMode:
            widget.toggleWidgetTextField() # ui_dataWidget method
        else:
            widget.toggleWidgetTextField(persistent=True) # ui_dataWidget method
        item.setSizeHint(widget.sizeHint())
        
    def closeInactiveItems(self, closeAll=False):
        count = self.getRowCount()
        for row in range(count):
            if row != self.getCurrentRow() or closeAll:
                item = self.getItem(row)
                widget = self.getItemWidget(item)
                widget.toggleWidgetTextField(setHidden=True) # ui_dataWidget method
                item.setSizeHint(widget.sizeHint())
    
    def getCurrentWidget(self):
        item = self.getCurrentItem()
        widget = self.getItemWidget(item)
        return widget
                
    def getRowCount(self):
        return self.ui.list_items.count()
    
    def getCurrentRow(self):
        return self.ui.list_items.currentRow()
    
    def setCurrentRow(self, row):
        self.ui.list_items.setCurrentRow(row)
    
    def getCurrentItem(self):
        return self.ui.list_items.currentItem()
    
    def getItem(self, row):
        return self.ui.list_items.item(row)
    
    def getItemWidget(self, item):
        return self.ui.list_items.itemWidget(item)
    
    def removeCurrentRow(self):
        row = self.getCurrentRow()
        self.ui.list_items.takeItem(row)
        
    def getNewNameText(self):
        return self.ui.newName.text()
    
    def clearNewNameText(self):
        self.ui.newName.setText('')
              

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())
            