from tkinter import *
from tkinter import Button
from Player import Player


class PlayerKiller(Button):

    def __init__(self, player:Player, **options):
        super().__init__(command = self.playerKillerCommand, **options)
        self.player = player

    def playerKillerCommand(self):
        import init
        import Playermanager
        self.player.setAlive(False)
        self.player.configure(bg = 'red', state = DISABLED)
        self.configure(state = DISABLED)
        Playermanager.Playermanager.numberDeadPlayers += 1
        if Playermanager.Playermanager.numberDeadPlayers == 7:
            init.issaFirst()
        Playermanager.Playermanager.removeDead()