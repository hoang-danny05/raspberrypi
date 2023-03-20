from re import X
from PyQt5 import QtWidgets

#passed command line arguments given to our script
app = QtWidgets.QApplication([])

#first widget
#widgets refer to visible components
window = QtWidgets.QWidget()
#setting property
window.setWindowTitle("Hello QT!!")
#getting property
print(window.windowTitle())

window.show()

app.exec()

