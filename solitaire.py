from card import Card
from cardpile import CardPile
from deckpile import DeckPile
from discardpile import DiscardPile
from suitpile import SuitPile
from tablepile import TablePile

from tkinter import *

# What are the funny shaped blue squares at the top?

# When I pick up a card in the table pile, move it in the
# same click, and clean up where the card was.
# The Discard Pile does this correctly.


class Solitaire(Frame):

    # Should these be static???
    deckPile = []
    discardPile = []
    tableau = []
    suitPile = []
    cardPile = []  # CardPile

    frameWidth = 450
    frameHeight = 600
    deckPileX = 335
    deckPileY = 30
    discardPileX = 268
    discardPileY = 30
    suitPileY = 30
    tablePileY = Card.height + 35
    cardPileSize = 13
    suitPileSize = 4
    tableauSize = 7

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Python Solitaire!!")
        self.master.geometry("600x600")

        # Restart
        self.restart_button = Button(self, text="Restart", command=self.init)
        self.restart_button.pack(side=BOTTOM)

        self.myCanvas = Canvas(self, width=400, height=400, background="bisque")
        self.myCanvas.pack(side="bottom", fill="both", expand=True)

        self.myCanvas.bind("<Button-1>", self.mouse_pressed)

        self.allPiles = []

        self.init()

        print("Deckpile size is: ", len(self.deckPile.thePile))
        print("Discardpile size is: ", len(self.discardPile.thePile))

        # print size of 7 table piles
        # add 4 suitpiles

    def init(self):
        print("in init")
        # change self to Solitaire
        # then fill the arrays in

        self.deckPile = DeckPile(Solitaire.deckPileX, Solitaire.deckPileY, self, self.myCanvas)
        self.allPiles.append(self.deckPile)
        self.discardPile = DiscardPile(Solitaire.discardPileX, Solitaire.discardPileY, self, self.myCanvas)
        self.allPiles.append(self.discardPile)

        for i in range(4):
            self.suitPile.append(SuitPile(15 + (Card.width + 10) * i, Solitaire.suitPileY, self.myCanvas))
            self.allPiles.append(Solitaire.suitPile[i])

        for i in range(7):
            self.tableau.append(TablePile(15 + (Card.width + 5) * i, Card.height + 35, i + 1, self, self.myCanvas))
            self.allPiles.append(self.tableau[i])

        for i in range(13):
            self.allPiles[i].display()
        '''
        self.deckPile.display()
        self.discardPile.display()
        self.suitPile[0].display()
        self.suitPile[1].display()
        self.suitPile[2].display()
        self.suitPile[3].display()
        self.tableau[0].display()
        self.tableau[1].display()
        self.tableau[2].display()
        self.tableau[3].display()
        self.tableau[4].display()
        self.tableau[5].display()
        self.tableau[6].display()
        '''
    # @staticmethod
    def mouse_pressed(self, event):
        # get mouse click position
        x = event.x
        y = event.y
        for i in range(13):
            if self.allPiles[i].includes(x, y):
                self.allPiles[i].select(x, y)

            self.allPiles[i].display()


if __name__ == "__main__":
    Solitaire().mainloop()
