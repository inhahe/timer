This is a tool written in Python using Pygame that allows you to set a timer on the command-line, which plays a sound after the specified number of numbers of minutes/seconds/hours.

Usage: 

timer &lt;number-of-seconds>

or

timer &lt;number-of-minutes:number-of-seconds>

or

timer &lt;number-of-hours:number-of-minutes:number-of-seconds>

Includes a .bat file that makes it easier to invoke on Windows and displays the current time when you invoke the timer (which should really be done in the program itself). The .bat file has my path to python.exe hard-coded; it would probably be better if that were changed to simply "python.exe"
