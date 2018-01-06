from PyQt5.QtWidgets import QListWidgetItem, QWidget, QLabel, QPushButton, QHBoxLayout, QLayout

class dataWidget(QWidget):
    def __init__(self, paramDict):
        super().__init__()
        self.params =   {
                        'title':'None',
                        'expanded':'False',
                        'data':'None'
                        }
        self.params.update(paramDict)
        
        self.listItem = QListWidgetItem()
        self.title = QLabel(self.params['title'])
        self.button = QPushButton(self.params['data'])
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.button)
        self.layout.addStretch()
        self.layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(self.layout)  
        self.listItem.setSizeHint(self.sizeHint())