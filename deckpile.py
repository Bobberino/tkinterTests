
#
# Created by Robert on 5/13/2014.
#

import random
from card import Card
from cardpile import CardPile


class DeckPile(CardPile):

    def __init__(self, x, y, main, canvas):
        # first initialize parent
        super().__init__(x, y, canvas)
        self.canvas = canvas
        self.main = main
        # then create new deck

        #########################
        for i in range(4):
            for j in range(13):
                # use add_card??
                self.add_card(Card(i, j))  # Card needs canvas as third parm

        # shuffle the list
        # load the deque from the shuffled list
        # shuffle the cards
        random.shuffle(self.thePile)

    def select(self, tx, ty):
        # if self.thePile.is_empty():
        if self.is_empty():  # self.empty
            return

        temp = self.thePile.pop()
        self.main.discardPile.add_card(temp)

