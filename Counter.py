from Displays import *
from Button import *
import time

""" 
This is a counter class that will implement a basic
increment-reset counter and show the count on a display
"""

class Counter:


    def __init__(self):
        print("Counter: constructor")
        self._number = 0

        self._display = LCDDisplay(sda= 20,scl = 21, i2cid = 0 )

        self._greenButton = Button(17, "increase", buttonhandler=self, lowActive=True)
        self._redButton = Button(16, "reset", buttonhandler=self, lowActive=True)

    def increment(self):
        print("Counter: incrementing")
        self._number = self._number + 1

    def reset(self):
        print("Counter: resetting")
        self._number = 0
        self._display.reset()

    def buttonPressed(self, name):
        if name == "increase":
            self.increment()
        elif name == "reset":
            self.reset()

    def buttonReleased(self, name):
        pass

    def show(self):
        while True:
            self._display.showNumber(self._number)
            time.sleep(0.1)
