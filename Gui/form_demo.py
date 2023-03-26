import sys
from PyQt5 import QtWidgets, QtGui, QtCore

#class for the main window
class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        #MainWindow Constructor
        super().__init__()
        #Custom Code Start
        form_layout = QtWidgets.QFormLayout()
        self.setLayout(form_layout)
        #setting the title 
        form_layout.addRow(QtWidgets.QLabel("Really cool form"))
        #setting first input
        self.line1 = QtWidgets.QLineEdit(self)
        form_layout.addRow("Name: " , self.line1)

        #Custom Code End
        self.show()

#only executes if thsi file is explicitly called
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
