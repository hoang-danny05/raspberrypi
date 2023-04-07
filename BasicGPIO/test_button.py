#this is a comment
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
import RPi.GPIO as GPIO
#initialize Raspberry pi
GPIO.setmode(GPIO.BOARD)
pin = 7
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#class for the main window
class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        #MainWindow Constructor
        super().__init__()
        #Custom Code Start
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("Button Detector.")
        layout = QtWidgets.QFormLayout()
        self.setLayout(layout)

        label = QtWidgets.QLabel("Circuit Status:", self)
        label.setFont(QFont("Arial", 30))
        layout.addRow(label)

        self.label2 = QtWidgets.QLabel("NOT PRESSED", self)
        self.label2.setFont(QFont("Arial", 30))
        layout.addRow(self.label2)

        self.clock = QtCore.QTimer()
        self.clock.setInterval(500)
        self.clock.timeout.connect(self.check_state)
        self.clock.start()
        #Custom Code End
        #widget calls its show method, it becomes the top level window
        self.show()

    def check_state(self ):
        print(f"Button State: {GPIO.input(pin)}")
        self.label2.setText("PRESSED" if not GPIO.input(pin) else "NOT PRESSED")

#only executes if thsi file is explicitly called
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    res = app.exec()
    print("closed")
    GPIO.cleanup()
    sys.exit(res)
