import sys
from PyQt5 import QtWidgets, QtGui, QtCore

#class for the main window
class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        #MainWindow Constructor
        super().__init__()
        ############################Custom Code Start
        self.setGeometry(100,100,300,300)

        form_layout = QtWidgets.QFormLayout()
        self.setLayout(form_layout)

        form_layout.addRow(QtWidgets.QLabel("<b>Really cool form</b>", self))

        self.line1 = QtWidgets.QLineEdit(self)
        form_layout.addRow("Name: " , self.line1)

        self.button : QtWidgets.QPushButton = QtWidgets.QPushButton("Submit", self)
        self.button.clicked.connect(self.onsubmit)
        form_layout.addRow(self.button)

        self.outputlabel = QtWidgets.QLabel("", self)
        form_layout.addRow(self.outputlabel)
        #Custom Code End
        self.show()

    def onsubmit(self, _):
        name = self.line1.text()
        print(name)
        self.outputlabel.setText(f"Hello, {name}")


#only executes if thsi file is explicitly called
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
