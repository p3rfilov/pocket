import os
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLayout, QTextEdit
from PyQt5 import QtCore, QtGui

class dataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.defaults = {'name':'New Note', 'data':'None'}
        self.editState = False
        self.dir = os.path.dirname(__file__)
        
        self.name = QLabel(self.defaults['name'])
        
        self.delButton = QPushButton('')
        self.delButton.setMaximumSize(23, 23)
        self.delButton.setIcon(QtGui.QIcon(os.path.join(self.dir, '../images/del Button.png')))
        self.delButton.setIconSize(QtCore.QSize(20,20))
        self.delButton.setFlat(True)
        self.delButton.hide()
        
        self.textEdit = QTextEdit(self.defaults['data'])
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.hide()
        
        self.editButton = QPushButton('edit')
        self.editButton.setMaximumSize(45, 20)
        self.editButton.hide()
        
        self.okButton = QPushButton('ok')
        self.okButton.setMaximumSize(45, 20)
        self.okButton.hide()
        
        self.cancelButton = QPushButton('cancel')
        self.cancelButton.setMaximumSize(45, 20)
        self.cancelButton.hide()
        
        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        
        self.layout2.addWidget(self.name)
        self.layout2.addStretch()
        self.layout2.addWidget(self.delButton)
        
        self.layout3.addStretch()
        self.layout3.addWidget(self.editButton)
        self.layout3.addWidget(self.okButton)
        self.layout3.addWidget(self.cancelButton)
        
        self.layout1.addLayout(self.layout2)
        self.layout1.addWidget(self.textEdit)
        self.layout1.addLayout(self.layout3)
        self.layout2.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(self.layout1)
        
    def toggleWidgetTextField(self, setHidden=False, persistent=False):
        def showAll():
            self.textEdit.show()
            self.delButton.show()
            self.editButton.show()
        
        if persistent: showAll()
        elif not setHidden and self.textEdit.isHidden():
            showAll()
        else:
            self.setEditState(False)
            self.textEdit.hide()
            self.delButton.hide()
            self.editButton.hide()
        self.resize(QtCore.QSize(0,0))
            
    def setName(self, name):
        self.name.setText(name)
        
    def setNotes(self, data):
        self.textEdit.setText(data)
        
    def getName(self):
        return self.name.text()
    
    def getNotes(self):
        return self.textEdit.toPlainText()
    
    def setEditState(self, state):
        self.editState = state
        if state:
            self.editButton.hide()
            self.okButton.show()
            self.cancelButton.show()
            self.textEdit.setReadOnly(False)
            self.textEdit.setFocus()
        else:
            self.editButton.show()
            self.okButton.hide()
            self.cancelButton.hide()
            self.textEdit.setReadOnly(True)
            
    def getEditState(self):
        return self.editState
        
    
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    window = dataWidget()
    window.show()
    window.toggleWidgetTextField(setHidden=False)
    sys.exit(app.exec_())
        
    