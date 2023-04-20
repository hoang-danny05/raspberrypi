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
        #Main Window Attributes ////////////////
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Button Clicker.")
        self.setStyleSheet("background-color: #333;")

        layout = QtWidgets.QFormLayout()
        self.setLayout(layout)
        #Subwidgets //////////////////////////////
        #Row 1
        scene = QtWidgets.QGraphicsScene(0,0,50,50)

        img = QtWidgets.QLabel("<img src='Mecademic/Screenshot from 2023-04-19 17-36-50.png' width=25>", self)

        title = QtWidgets.QLabel("Mecademic Code", self)
        title.move(50,50)
        title.setFont(QtGui.QFont("default", 16))
        title.setStyleSheet("margin-left: 20px;color: white;")
        layout.addRow(img, title)

        self.button = QtWidgets.QPushButton("x", self, 
            checkable=True, 
            checked=False
        )
        self.button.setStyleSheet("color: white;")
        self.button.move(50,100)
        #Custom Code End
        #widget calls its show method, it becomes the top level window
        self.show()


#only executes if thsi file is explicitly called
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    res = app.exec()
    print("closed")
    sys.exit(res)
