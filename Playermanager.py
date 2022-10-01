from tkinter.constants import DISABLED, NORMAL
from tkinter import *
from Player import Player
from PlayerKiller import PlayerKiller

class Playermanager():
    queuesize = 4
    numberDeadPlayers = 0
    allPlayers = set()
    playerKillerSet = set()
    playablePlayers = set()
    deadPlayers = set()
    nonPlayablePlayers = []

    @classmethod
    def addPlayer(cls, player:Player):
        cls.allPlayers.add(player)
        cls.playablePlayers.add(player)
        player.setAlive(True)

    @classmethod
    def killPlayer(cls, player:Player):
        cls.playablePlayers = cls.playablePlayers | set(cls.nonPlayablePlayers)
        cls.nonPlayablePlayers = []
        cls.deadPlayers.add(player)

    @classmethod
    def reset(cls):
        cls.queuesize = 4
        cls.numberDeadPlayers = 0
        cls.playablePlayers = cls.playablePlayers | cls.deadPlayers | set(cls.nonPlayablePlayers)
        cls.deadPlayers = set()
        cls.nonPlayablePlayers = []
        for player in cls.playablePlayers:
            player.setAlive(True)
            player.configure(bg = 'SystemButtonFace', state = NORMAL)
        for playerKiller in cls.playerKillerSet:
            playerKiller.configure(state = NORMAL)

    @classmethod
    def resizeQueue(cls):
        cls.queuesize = max(0, 4-len(cls.deadPlayers))
    
    @classmethod
    def configurePlayerButtons(cls):
        for button in cls.playablePlayers:
            button.configure(state = NORMAL, bg = 'SystemButtonFace')
        for button in cls.nonPlayablePlayers:
            button.configure(state = DISABLED, bg = 'grey')

    @classmethod
    def removeDead(cls):
        for p in cls.playablePlayers:
            if p.getAlive() == False:
                cls.killPlayer(p)
                cls.playablePlayers.remove(p)
        for p in cls.nonPlayablePlayers:
            if p.getAlive() == False:
                cls.killPlayer(p)
                cls.nonPlayablePlayers.remove(p)
        cls.resizeQueue()
        cls.configurePlayerButtons()

    @classmethod
    def roundLoop(cls, player: Player):
        cls.resizeQueue()
        if cls.queuesize == 0:
            pass
        elif len(cls.nonPlayablePlayers) == cls.queuesize:
            cls.playablePlayers.add(cls.nonPlayablePlayers.pop(0))
            cls.nonPlayablePlayers.append(player)
        elif len(cls.nonPlayablePlayers) < cls.queuesize:
            cls.nonPlayablePlayers.append(player)
        else:
            print("wtf just happened!??")
        cls.configurePlayerButtons()

def you_shall_not():
    pass