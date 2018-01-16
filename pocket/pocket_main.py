from ui_dataWidget import dataWidget
from ui_mainWindow import mainWindow

class pocket_main():
    def __init__(self):
        self.window = mainWindow()
        
    def addNewPocket(self, params):
        widget = dataWidget()
        widget.setTitle(params['name'])
        widget.setData(params['data'])
        
        widget.delButton.clicked.connect(self.removeRow)
        widget.editButton.clicked.connect(lambda: widget.setEditState(True))
        widget.cancelButton.clicked.connect(lambda: widget.setEditState(False))
        
        self.window.addNewRow(widget)
        

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)       
    pocket = pocket_main()
    sys.exit(app.exec_())