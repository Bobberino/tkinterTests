from card import Card

from tkinter import *


class SimpleFrame(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Simple Frame!!")
        self.master.geometry("500x500")

        # Restart
        self.restart_button = Button(self, text="Restart", command=self.init)
        self.restart_button.pack(side=BOTTOM)

        self.myCanvas = Canvas(self)
        self.myCanvas.pack()  # side = BOTTOM

        self.myCanvas.bind("<Button-1>", self.mouse_pressed)

        self.init()

    def init(self):
        print("restarting")

        card = Card(0, 0)
        card.flip()
        card.draw(300, 200, self.myCanvas)

    @staticmethod
    def mouse_pressed(event):
        # get mouse click position
        x = event.x
        y = event.y
        print("Mouse clicked position: ", x, y)


if __name__ == "__main__":
    SimpleFrame().mainloop()
