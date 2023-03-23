#this is a comment
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import RPi.GPIO as GPIO
#initialize Raspberry pi
power = 25
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm = GPIO.PWM(7,400)
pwm.start(0)

#class for the main window
class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        #MainWindow Constructor
        super().__init__()
        #Custom Code Start
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Button Clicker.")

        label = QtWidgets.QLabel("Toggle Circuit", self)
        label.move(50,50)

        self.button = QtWidgets.QPushButton("x", self, 
            checkable=True, 
            checked=False
        )
        self.button.clicked.connect(self.button_toggled) 
        self.button.move(50,100)
        #Custom Code End
        #widget calls its show method, it becomes the top level window
        self.show()

    def button_toggled(self, checked):
        print(f"Button State: {checked}")
        # print(f"a: {self} b: {checked}")
        if checked:
            pwm.ChangeDutyCycle(power)
        else:
            pwm.ChangeDutyCycle(0)

#only executes if thsi file is explicitly called
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    res = app.exec()
    print("closed")
    GPIO.cleanup()
    sys.exit(res)
