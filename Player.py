from tkinter import *
from tkinter import Button

class Player(Button):
    
    def __init__(self, name, **options):
        super().__init__(command = self.foo, **options)
        self.name = name
        self.alive = True

    def getName(self):
        return self.name

    def getAlive(self):
        return self.alive

    def setAlive(self, alive):
        self.alive = alive

    def foo(self):
        import Playermanager
        Playermanager.Playermanager.roundLoop(self)