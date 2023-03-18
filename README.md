Hello Jared! 
I have included three files that you can copy to your Raspberry Pi.

some terminal tips are also included at the end.

##FILE1: TURNON.PY

this file is simple, it just turns on GPIO4 for 10 seconds. Use this file to test if GPIO4 is actually working.
The red wire of the speaker should be connected to GPIO4, The black wire of the speaker should be connected to GND.

when you run the program, the speaker should turn on. When the program ends, the speaker should be off. If the Raspberry Pi does not work like this, the circuit is connected incorrectly.

##FILE2: BEEPBEEP.PY

This file simply turns GPIO4 on and off for 10 times.

##FILE3: VOLUME.PY

this file makes a PWM (pulse width modulator: turns voltage on and off really fast to simulate a lower voltage) to control the volume of the speaker.

You can control the volume of the speaker by editing the code or inserting it in the command line

*duty_cycle = 10*
change this ^ to change the default volume of the speaker

*> python filename.py 40*
enter this in the terminal ^ to input a volume percentage. Changing this does the same thing as changing the duty cycle, but its a lot faster

##terminal tricks

every terminal has its location. If you want to see every file in your current location (directory), type: 
*> ls*
This tells you the names of all the files and folders that is in your current location. 
CD lets you change locations to other folders/directories
*> cd Documents*
*> cd ../*
this ^ changes you to the parent folder
to change the name of a file, use the mv command
*> mv badfilename.py volume.py*
this ^ renames badfilename.py to volume.py. it stands for move