from tkinter import *
from tkinter import messagebox
from Player import Player
from PlayerKiller import PlayerKiller
from Playermanager import Playermanager

def iDied():
    if Playermanager.numberDeadPlayers <= 3:
        messagebox.showinfo("", "its all good. ull get your LP back, king <3")
        frame.quit()
        quit()
    else:
        messagebox.showinfo("", "Top 4 = LP go up :)")
        frame.quit()
        quit()

def issaFirst():
    messagebox.showinfo("","ISSA FIRST, LETS GOOOOO!!!")
    quit()

if __name__ == "__main__":
    
    #Sets up window and shit
    frame = Tk()
    frame.title("TFTracker")
    resetButton = Button(frame, text="Reset", command = Playermanager.reset)
    iDiedButton = Button(frame, text="I died.", command = iDied)
    playerLabel = Label(frame, text="Players:")

    resetButton.grid(row=0, column=0)
    iDiedButton.grid(row=0, column=1)
    playerLabel.grid(row=1, column=0)

    #Adds players and playerkillers to the gui
    for i in range(7):
        pname = f"Player {i+1}"
        p = Player(pname, text=pname, width=12)
        pk = PlayerKiller(p, text=f"{pname} died.", width=12)
        Playermanager.addPlayer(p)
        p.grid(row=i+2, column=0)
        Playermanager.playerKillerSet.add(pk)
        pk.grid(row=i+2, column=1)

    frame.mainloop()