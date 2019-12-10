# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: dicegame, program code template, version 2 (GUI components in in lists)

from tkinter import *
import random
import time


DICEPICS = [ "1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif" ]

PLAYER_NUMBER = 2
DICE_NUMBER = 3
THROW_TURNS = 2


class Dicegame:
    def __init__(self):
        self.__current_dice_score = []
        self.__window = Tk()
        self.__window.title("Dicegame")

        self.__turn = 0
        self.__player_points = [0] * PLAYER_NUMBER

        self.__dicepics = []
        for picfile in DICEPICS:
            pic = PhotoImage(file=picfile)
            self.__dicepics.append(pic)

        # These texts are only displayed in the window. We don't need to
        # modify them during the execution of the program so we don't store
        # them as attributes.
        for i in range(PLAYER_NUMBER):
            Label(self.__window, text="Player "+str(i+1)+" score:")\
            .grid(row=i+1, column=0, sticky=E)

        self.__infoLabel = Label(self.__window)
        self.__infoLabel.grid(row=PLAYER_NUMBER + 1, column=0, columnspan=2)

        self.__pointlabels = []
        for i in range(PLAYER_NUMBER):
            new_label = Label(self.__window)
            new_label.grid(row=i+1, column=1, sticky=W)
            self.__pointlabels.append(new_label)

        self.__dicepiclabels = []
        for i in range(DICE_NUMBER):
            new_label = Label(self.__window)
            new_label.grid(row=0, column=2+i)
            self.__dicepiclabels.append(new_label)

        self.__lockbuttons = []
        for i in range(DICE_NUMBER):
            new_button = Button(self.__window)
            new_button.grid(row=1, column=2+i)
            self.__lockbuttons.append(new_button)

        self.__throwButton = Button(self.__window, text="throw", command=self.throw)
        self.__throwButton.grid(row=0, column=DICE_NUMBER+2, sticky=W+E)
        self.__endturnButton = Button(self.__window, text="end turn", command=self.endturn)
        self.__endturnButton.grid(row=1, column=DICE_NUMBER+2, sticky=W+E)

        Button(self.__window, text="new game", command=self.initialize_game)\
            .grid(row=2, column=DICE_NUMBER+2, sticky=W+E+N)
        Button(self.__window, text="stop", command=self.__window.destroy)\
            .grid(row=4, column=DICE_NUMBER+2, sticky=W+E+S)

        self.initialize_game()

    def endturn(self): # TODO Clarify what means here the "turn"-term. Is it the turn in line or
        # how many times dice was thrown?
        self.__player_points[self.__turn] += sum(self.__current_dice_score)
        if self.__turn == 0:
            self.__turn = 1
        else:
            self.__turn = 0
        self.__gamesituationtext = "Player " + str(self.__turn + 1) + " turn"
        self.update_ui_texts()



    def initialize_game(self):
        self.__turn = 0
        self.__throwcount = THROW_TURNS
        self.__player_points = [0] * PLAYER_NUMBER
        self.__gamesituationtext = "Player "+str(self.__turn + 1) + " turn"

        # This list contains information on whether the dice is in use or not.
        self.__dices_in_use = [True] * DICE_NUMBER

        # This list contains the values of the dices, it can be used in 
        # calculating the points.
        self.__current_dice_score = [1] * DICE_NUMBER

        # Setting a picture of a dice showing 1 to all dicepicslabels. 
        for label in self.__dicepiclabels:
            label.configure(image=self.__dicepics[0])

        self.reset_lockbuttons()

        self.update_ui_texts()


    def reset_lockbuttons(self):
        # Setting all the lock buttons to their initial state.
        for button in self.__lockbuttons:
            button.configure(text="unlocked")     
            button.configure(background="green") 
            button.configure(state=NORMAL)      


    def update_ui_texts(self):
        # Displaying the players' scores in the UI.
        for i in range(len(self.__pointlabels)):
            self.__pointlabels[i].configure(text=self.__player_points[i])

        # Displaying the game status text in the UI.
        self.__infoLabel.configure(text=self.__gamesituationtext)

    def throw(self):
        """ Throw all dices """
        self.__current_dice_score.clear()
        for lbl in self.__dicepiclabels:
            number = random.randint(0,5)
            lbl.configure(image=self.__dicepics[number])
            self.__current_dice_score.append(number+1)

    def start(self):
        self.__window.mainloop()

def main():
    ui = Dicegame()
    ui.start()


main()
