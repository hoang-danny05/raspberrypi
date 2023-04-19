# MICROPYTHON ONLY from machine import Pin, I2C
from time import sleep
from max6675 import MAX6675
import sys
from PyQt5 import QtWidgets

#pinconfig

reader = MAX6675()

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        #custom code
        ##MAIN WINDOW LAYOUT
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("Reader")
        layout = QtWidgets.QFormLayout()
        self.setLayout(layout)

        label = QtWidgets.QLabel("<h1>MAX6675 Reader</h1>")
        layout.addRow(label)

        self.button = QtWidgets.QPushButton("Update")
        self.button.clicked.connect(self.update)
        layout.addRow(self.button)

        self.reading = QtWidgets.QLabel("__")
        layout.addRow(self.reading)
        #no more custom code
        self.show()

    def update(self):
        self.reading.setText(f"{reader.temp()} C")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec())
