from menu import *
from pygame import *
class Game():
    def __init__(self):
        # GAMES'S STATES: {Running|Menu} 
        self.STATES = {0:'Running', 1:'Menu'}
        self.npointer = 1
        self.CURRENT_STATES = self.STATES[self.npointer]
        self.GameQuit = False        
        
    def toggle(self):
        self.npointer = (self.npointer + 1) % len(self.STATES)
        self.CURRENT_STATES = self.STATES[self.npointer]
        
   
            
        