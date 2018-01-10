from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLayout, QTextEdit
from PyQt5 import QtCore

class dataWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.defaults = {'title':'New Note', 'data':'None'}
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
        self.editButton.setMaximumSize(35, 20)
        self.editButton.hide()
        
        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        
        self.layout2.addWidget(self.title)
        self.layout2.addStretch()
        self.layout2.addWidget(self.delButton)
        
        self.layout3.addStretch()
        self.layout3.addWidget(self.editButton)
        
        self.layout1.addLayout(self.layout2)
        self.layout1.addWidget(self.textEdit)
        self.layout1.addLayout(self.layout3)
        self.layout2.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(self.layout1)
        
        
    def toggleWidgetTextField(self, hide=False):
        if not hide:
            if self.textEdit.isHidden():
                self.textEdit.show()
                self.delButton.show()
                self.editButton.show()
                self.resize(QtCore.QSize(0,0))
                #self.resize(QtCore.QSize(self.sizeHint().width(), self.heightMax))
            else:
                self.textEdit.hide()
                self.delButton.hide()
                self.editButton.hide()
                self.resize(QtCore.QSize(0,0))
                #self.resize(QtCore.QSize(self.sizeHint().width(), self.heightMin))
        else:
            self.textEdit.hide()
            self.delButton.hide()
            self.editButton.hide()
            
    def setTitle(self, title):
        self.title.setText(title)
        
    def setData(self, data):
        self.textEdit.setText(data)
        
    