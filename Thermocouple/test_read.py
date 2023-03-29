import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        #MainWindow Constructor
        super().__init__()
        #Custom Code Start
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("Max6675 Reader")

        self.label = QtWidgets.QLabel("Reader", self)

        self.button = QtWidgets.QPushButton("Read Temperature", self)
        self.button.clicked.connect() #READ TEMPERATURE

        self.label = QtWidgets.QLabel("XX", self)
        #Custom Code End
        self.show()

    def read(self):
        print("reading")
        #use imported gpio pins

#only executes if thsi file is explicitly called
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())