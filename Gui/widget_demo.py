#this is a comment
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

#class for the main window
class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        #MainWindow Constructor
        super().__init__()
        #Custom Code Start
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Example Window")
        label = QtWidgets.QLabel("hello, world!", self)
        label.move(50,50)
        button = QtWidgets.QPushButton("hello", self)
        button.move(50,100)
        button.clicked.connect(lambda : print("Button Clicked"))
        #Custom Code End
        #widget calls its show method, it becomes the top level window
        self.show()

#only executes if thsi file is explicitly called
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
