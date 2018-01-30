import unittest
import sys
from PyQt5.QtWidgets import QApplication
from pocket.ui_dataWidget import dataWidget
from pocket.ui_mainWindow import mainWindow
from pocket.dataStore import dataStore


class TestUI(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = mainWindow()
        self.data = {'name':'Note ','data':'Some text '}
        self.cycles = 10
        
    def RUN_LOOP(self):
        try: sys.exit(self.app.exec_())
        except: pass
    
    def tearDown(self):
        pass
    
    def testDataWidget(self):
        widget = dataWidget()
        
        widget.toggleWidgetTextField()
        self.assertFalse(widget.textEdit.isHidden())
        self.assertFalse(widget.delButton.isHidden())
        self.assertFalse(widget.editButton.isHidden())
        
        widget.toggleWidgetTextField(setHidden=False)
        self.assertTrue(widget.textEdit.isHidden())
        self.assertTrue(widget.delButton.isHidden())
        self.assertTrue(widget.editButton.isHidden())
        
        widget.setName(self.data['name'])
        self.assertEqual(widget.getName(), self.data['name'])
        widget.setNotes(self.data['data'])
        self.assertEqual(widget.getNotes(), self.data['data'])
        
        widget.setEditState(True)
        self.assertTrue(widget.editButton.isHidden())
        self.assertFalse(widget.okButton.isHidden())
        self.assertFalse(widget.cancelButton.isHidden())
        self.assertTrue(widget.getEditState())
        
    def testMainWindow(self):
        window = mainWindow()
        widget = dataWidget()
        self.assertEqual(window.getRowCount(), 0)
        for i in range(self.cycles):
            window.addNewRow(widget)
        self.assertEqual(window.getRowCount(), self.cycles)
    
    def testAddNewPocket(self):
        for i in range(self.cycles):
            self.widget = dataWidget()
            self.widget.setName(self.data['name'] + str(i))
            self.widget.setNotes(self.data['data'] + str(i))
            self.window.addNewRow(self.widget)
#         self.RUN_LOOP()
            
    def testCheckPocketParameters(self):
        count = self.window.getRowCount()
        for row in range(count):
            item = self.window.getItem(row)
            widget = self.window.getItemWidget(item)
            self.assertEqual(widget.getTitle(), self.data['name'] + str(row))
            self.assertEqual(widget.getNotes(), self.data['data'] + str(row))
            
            
class testDataStore(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    


if __name__ == '__main__':
    unittest.main()
    