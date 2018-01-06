import sys
from PyQt5.QtWidgets import QApplication
from mainWindow import mainWindow

app = QApplication(sys.argv)
window = mainWindow()
sys.exit(app.exec_())