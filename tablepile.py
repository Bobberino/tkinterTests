# import java.awt.*;

#
# Created by Robert on 5/13/2014.
#

from card import Card
from cardpile import CardPile


class TablePile(CardPile):
    def __init__(self, x, y, c, main, canvas):
        super().__init__(x, y, canvas)
        self.canvas = canvas
        self.main = main

        for i in range(c):   # this needs to be c after testing
            temp_card = self.main.deckPile.pop()  # type needs to be Card
            self.add_card(temp_card)

        # flip topmost card face up
        self.top().flip()

    def includes(self, tx, ty):
        # don't test bottom of card
        return self.x <= tx and \
               tx <= (self.x + Card.width) and \
               self.y <= ty

    def can_take(self, a_card):
        if len(self.thePile) == 0:
            return a_card.rank() == 12

        top_card = self.top()
        return (a_card.color() != top_card.color()) and \
               (a_card.rank() == top_card.rank() - 1)

    def select(self, tx, ty):
        if self.is_empty():
            return

        # if face down, then flip
        top_card = self.top()
        if not top_card.faceUp():
            print("if not top_card.faceUp()")
            top_card.flip()
            print("Top card flipped, returning...")
            return

            # See if any suit pile can take top card
        top_card = self.pop()
        for sp in self.main.suitPile:
            if sp.can_take(top_card):
                sp.add_card(top_card)
                return

        for tb in self.main.tableau:
            print("For tb in self.main.tableau")
            if tb.can_take(top_card):
                print("tb.can_take(top_card_)")
                tb.add_card(top_card)
                print("tb.add_card(top_card)")
                return

        # else put it back on our pile
        self.add_card(top_card)

    def display(self):
        local_y = self.y
        for aCard in self.thePile:
            aCard.draw(self.x, local_y, self.canvas)
            local_y += 35

