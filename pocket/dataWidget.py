from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLayout, QTextEdit

class dataWidget(QWidget):
    def __init__(self, data={}):
        super().__init__()
        self.params =   {
                        'title':'New Note',
                        'expanded':'False',
                        'data':'None'
                        }
        self.params.update(data)
        
        self.title = QLabel(self.params['title'])
        
        self.button = QPushButton('-')
        self.button.setMaximumSize(17, 17)
        self.button.clicked.connect(self.setTextHidden)
        
        self.textEdit = QTextEdit(self.params['data'])
        self.textEdit.hide()
        
        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.title)
        self.layout2.addStretch()
        self.layout2.addWidget(self.button)
        self.layout1.addLayout(self.layout2)
        self.layout1.addWidget(self.textEdit)
        self.layout2.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(self.layout1)
        
    def setTextHidden(self):
        if self.textEdit.isHidden():
            self.textEdit.show()
        else:
            self.textEdit.hide()