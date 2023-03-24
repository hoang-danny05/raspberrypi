# Raspberry Pi Files

## BasicGPIO
Hello Jared! 
I have included three files that you can copy to your Raspberry Pi.

some terminal tips are also included at the end.

This is a collection of Python files that test the RPi.GPIO module. 

### turnon.py

this file is simple, it just turns on GPIO4 for 10 seconds. Use this file to test if GPIO4 is actually working.
The red wire of the speaker should be connected to GPIO4, The black wire of the speaker should be connected to GND.

when you run the program, the speaker should turn on. When the program ends, the speaker should be off. If the Raspberry Pi does not work like this, the circuit is connected incorrectly.

### beepbeep.py

This file simply turns GPIO4 on and off for 10 times.

### volume.py

this file makes a PWM (pulse width modulator: turns voltage on and off really fast to simulate a lower voltage) to control the volume of the speaker.
You can control the volume of the speaker by editing the code or inserting it in the command line

```python
duty_cycle = 10
```

change this ^ to change the default volume of the speaker

```bash
python filename.py 40
```

enter this in the terminal ^ to input a volume percentage. Changing this does the same thing as changing the duty cycle, but its a lot faster

## Gui - PyQt5

This is a collection of Python files that use PyQt5 to create small GUI applications to manage the

### qt_template.py

this is a template file that makes a class called __MainWindow()__ to easily sort the code of the main window.

```python
class MainWindow(QtWidgets.QtWidgets):
    def __init__(self):
        #MainWindow Constructor
        super().__init__()
        #Custom Code Start

        #Custom Code End
        self.show
```

You declare all other widgets where "Custom Code Start" is.

### test_button.py

This file merges functionality with the RPi.GPIO library and PyQt5. This file demonstrates how to pass in functions as __callbacks__, and how to run code on the PyQt app's exit. 

```python
class MainWindow(QWidgets.QWidget):
    def __init__(self):
        ...
        self.button = QtWidgets.QPushButton("x", self, 
            checkable=True, 
            checked=False
        )
        self.button.clicked.connect(self.button_toggled) 
        #the button will call button_toggled(self, bool) when clicked
        ...
    def button_toggled(self, checked):
        print(f"state: {checked}")
        #code that runs whenever the button is clicked
```

as demonstrated by the code above, you can define callback functions that would be called once the button is clicked. Alternatively, if the function that you want to execute is small (meaning that it only consists of one line), then you may use [lambda](https://sparkbyexamples.com/python/python-lambda-function/) functions. 

```python
self.button.clicked.connect(lambda self, checked: print(f"state: {checked}")
```


## terminal tips

__ls command__:
every terminal has its location. If you want to see every file in your current location (directory), type: 

```sh
ls
```

__cd command__:
This tells you the names of all the files and folders that is in your current location. 
CD lets you change locations to other folders/directories

```sh
cd Documents
```

```sh
cd ../
```

this ^ changes you to the parent folder

__mv command__:
to change the name of a file, use the mv command

```sh
mv badfilename.py volume.py
```

this ^ renames badfilename.py to volume.py. it stands for move
