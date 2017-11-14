from Android2 import Android
from graphics import *

class BabyAndroid(Android):
    def __init__(self, win, colour, headCentreX, headCentreY):
        Android.__init__(self, win, colour, headCentreX, headCentreY, 0.8, 0.0001)
            
        self.cryMessage = Text(Point(0.5, 0.75), "")
        self.cryMessage.setSize(20)
        self.cryMessage.draw(win)
        
    def cry(self):
        self.cryMessage.setText("Baby Android Says: Waaaaa!!!")
        
    def stopCrying(self):
        self.cryMessage.setText("")