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
        #MAINWINDOW
        self.setGeometry(100,100, 300,300) #x, y, width, height
        self.setWindowTitle("Grid Template Demo")
        #BODY
        label1 = QtWidgets.QLabel("Text1")
        label2 = QtWidgets.QLabel("Text2")
        button1 = QtWidgets.QPushButton("x")
        button2 = QtWidgets.QSpinBox(self, value=100, prefix='$', singleStep=5, maximum=1000)
        #MAINWINDOW - LAYOUt
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        layout.addWidget(label1, 0, 0, 1, 2)
        layout.addWidget(label2, 1, 0, 1, 1)
        layout.addWidget(button1, 1, 1, 1, 1)
        layout.addWidget(button2, 0, 2, 2, 1)
        ##########GRID-LAYOUT#########
        # label1 | label1  | button2 #
        #----------------------------#
        # label2 | button1 | button2 #
        ##############################
        #Custom Code End
        self.show()

#only executes if thsi file is explicitly called
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
