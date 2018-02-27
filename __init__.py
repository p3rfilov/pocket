if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from components.pocket import pocket_main
    
    app = QApplication(sys.argv)       
    pocket = pocket_main()
    sys.exit(app.exec_())
