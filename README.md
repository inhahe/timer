This is a tool written in Python using Pygame that allows you to set a timer on the command-line, which plays a sound after the specified number of numbers of minutes/seconds/hours.

Usage: 

timer &lt;number-of-seconds>

or

timer &lt;number-of-minutes:number-of-seconds>

or

timer &lt;number-of-hours:number-of-minutes:number-of-seconds>

Includes a .bat file that makes it easier to invoke on Windows and displays the current time in the command window when you invoke the timer, which isn't done in the program itself because it's intended to be run using pythonw.exe. The .bat file has my path to python.exe hard-coded; it would probably be better if that were changed to simply "python.exe"

The path to the sound to play is also hard-coded into timer.py, so you'll have to change that too.
