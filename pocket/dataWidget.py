import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLayout, QTextEdit
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

class dataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.defaults = {'title':'New Note', 'data':'None'}
        self.editState = False
        #self.heightMin = 35
        #self.heightMax = 100
        #self.resize(QtCore.QSize(self.sizeHint().width(), self.heightMin))
        
        self.title = QLabel(self.defaults['title'])
        
        self.delButton = QPushButton('x')
        self.delButton.setMaximumSize(17, 17)
        self.delButton.hide()
        
        self.textEdit = QTextEdit(self.defaults['data'])
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
        
        self.layout2.addWidget(self.title)
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
        
    def toggleWidgetTextField(self, setHidden=False):
        if not setHidden and self.textEdit.isHidden():
            self.textEdit.show()
            self.delButton.show()
            self.editButton.show()
        else:
            self.textEdit.hide()
            self.delButton.hide()
            self.editButton.hide()
        self.resize(QtCore.QSize(0,0))
            
    def setTitle(self, title):
        self.title.setText(title)
        
    def setData(self, data):
        self.textEdit.setText(data)
        
    def getTitle(self):
        return self.title.text()
    
    def getData(self):
        return self.textEdit.toPlainText()
    
    def setEditState(self, state):
        if state:
            self.editButton.hide()
            self.okButton.show()
            self.cancelButton.show()
        else:
            self.editButton.show()
            self.okButton.hide()
            self.cancelButton.hide()
            
    def getEditState(self):
        return self.editState
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = dataWidget()
    window.show()
    window.toggleWidgetTextField(setHidden=False)
    sys.exit(app.exec_())
        
    