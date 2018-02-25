from PyQt5.QtWidgets import QMessageBox

class Message():
    def __init__(self, parent=None):
        self.parent = parent
    
    def delete(self):
        reply = QMessageBox.question(self.parent, 'Sure?',"Delete this pocket?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False
        
    def duplicateRecord(self):
        QMessageBox.information(self.parent, 'Duplicate name',"A pocket with this name already exists!\nPlease try another name.")
        
    def rowOrderFail(self):
        QMessageBox.critical(self.parent, 'Bad row order',"Could not recreate custom row order!")
    

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    delMsg = Message().delete()
    dupMsg = Message().duplicateRecord()
    rowMsg = Message().rowOrderFail()
    sys.exit(app.exec_())