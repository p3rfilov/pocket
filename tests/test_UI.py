import unittest
import sys
from PyQt5.QtWidgets import QApplication
from pocket.ui_dataWidget import dataWidget
from pocket.ui_mainWindow import mainWindow

'''
TO DO:

Replace direct access to mainWindow components (self.window.ui.list_items) with function calls
'''

class TestUI(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = mainWindow()
        self.listWidget = self.window.ui.list_items
        
    def RUN_LOOP(self):
        try: sys.exit(self.app.exec_())
        except: pass
    
    def tearDown(self):
        pass
    
    def test_AddNewPocket(self):
        for i in range(20):
            data = {'name':'Note ' + str(i),'data':str(i)*200}
            widget = dataWidget()
            widget.setTitle(data['name'])
            widget.setData(data['data'])
            self.window.addNewRow(widget)
        self.RUN_LOOP()
            
    def test_CheckPocketParameters(self):
        for i in range(self.listWidget.count()):
            item = self.window.ui.list_items.item(i)
            widget = self.window.ui.list_items.itemWidget(item)
            self.assertEqual(widget.getTitle(), 'Note ' + str(i))
            self.assertEqual(widget.getData(), str(i)*200)


if __name__ == '__main__':
    unittest.main()
    