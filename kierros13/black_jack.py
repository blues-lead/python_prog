######## Black Jack peli ###############################
######## Anton Kondratev, 282650 #######################
######## TIE-02101, Ohjelmointi 1 ######################
# Pelisäännöt: Pelin tavoitteena on saada 21 pistettä. Pelaaja, jonka pistemäärä on yli 21 häviää pelin.
# Jos molempien pelaajien pistemäärät ovat vähemmän tai yhtä suuri kuin 21, niin enemmän pisteitä kerännyt voittaa.
# Käyttäjä aloittaa pelin. Aluksi käyttäjällä on kaksi korttia ja jokainen kortti vastaa tiettyä pistemäärä.
# (Kortit ja niitä vastaavat pistemäärät ovat tiedostossa giffit/pics.txt). Käyttäjä voi ottaa lisää kortteja
# painamalla "More..."-painiketta. Kun käyttäjän pistemäärä on enemmän tai yhtäsuuri kuin 21 vuoro siirtyy tietokoneelle.
# Tietokone pelaa samalla tavalla kuin käyttäjä.

from tkinter import *
from tkinter import messagebox as mb
import random
import time
from threading import Thread

MAX_PLAYED_CARD = 9 # pelaajan maximikorttimäärä, 17 >= MAX_PLAYED_CARD >= 9
GAME_FILE = "giffit/pics.txt" # tiedosto, jossa ovat kortit ja pisteet

class BJ:
    def __init__(self):
        self.__winner = "" # sisältää tiedot voittajasta
        self.__cards = {} # pitää sisällään kaikki kortit ja pisteet
        self.__window = Tk()
        self.__window.title("Black Jack")
        self.__window.configure(bg="green")
        self.__my_ims = [] # käyttäjän korttien kuvat
        self.__pc_ims = [] # tietokoneen korttien kuvat
        self.__testcard = PhotoImage(file="giffit/other/back_green.gif")
        self.__deck_label = Label(self.__window, image=self.__testcard, borderwidth=0)
        self.__deck_label.grid(row=1, column=2, columnspan=MAX_PLAYED_CARD+1)

        self.__mydeck = [] # käyttäjän label-kortit
        self.__mydeck_free = MAX_PLAYED_CARD # käyttäjän (alarivi) vapaiden paikkojen määrä
        for i in range(MAX_PLAYED_CARD):
            new_lbl = Label(self.__window, borderwidth=2, relief=GROOVE)
            new_lbl.grid(row=2,column=i+2)
            self.__mydeck.append(new_lbl)

        self.__cdeck = [] # tietokoneen label-kortit
        self.__cdeck_free = MAX_PLAYED_CARD # tietokoneen (ylärivi) vapaiden paikkojen määrä
        for i in range(MAX_PLAYED_CARD):
            new_lbl = Label(self.__window, borderwidth=2, relief=GROOVE)
            new_lbl.grid(row=0,column=i+2)
            self.__cdeck.append(new_lbl)

        # "More.."-painike: antaa käyttäjälle lisää yhden kortin
        self.__morebutton = Button(text="More...", height=2, width=10, command=self.__get_me_more)
        #self.__morebutton.grid(row=1, column=9)
        self.__morebutton.grid(row=1, column=MAX_PLAYED_CARD)

        # "Pass"-painike: antaa pelivuoron tietokoneelle
        # __pc_game_start will be performing in own thread
        self.__passbutton = Button(text="Pass", height=2, width=10, command=lambda: Thread(target=self.__pc_game_start).start())
        self.__passbutton.grid(row=1, column=MAX_PLAYED_CARD+1)

        # "Close"-painike: sulkee pääikkunan
        self.__closebutton = Button(text="Close", height=2, width=10, command=self._close)
        self.__closebutton.grid(row=1, column=2)

        # "New game"-painike: aloittaa peli uudestaan
        self.__newgamebutton = Button(text="New game", height=2, width=10, command=self.init_game)
        self.__newgamebutton.grid(row=1, column=3)

        # painikelista
        self.__buttons = [self.__morebutton, self.__passbutton, self.__closebutton, self.__newgamebutton]

        self.__p_one_label = Label(text="Player scores:") # käyttäjän pistemäärä label
        self.__p_one_label.grid(row=3, column=2)

        self.__pc_label = Label(text="PC scores:") # tietokoneen pistemäärä label
        self.__pc_label.grid(row=3, column=MAX_PLAYED_CARD + 1)

        self.init_game()

    def init_game(self):
        """
        Metodi aloittaa pelin: alustaa kaikki muuttujat, antaa käyttäjälle kaksi korttia
        ja laskee kortteja vastaavat pisteet muuttujaan self.__mypoints
        :return: ei palauta mitään
        """
        self.__winner = ""
        self.fill_card_deck(GAME_FILE)
        self.__release_gameButtons()
        self.__mypoints = 0
        self.__cpoints = 0
        self.__im = PhotoImage(file="giffit/other/Green.gif")
        self.__mydeck_free = MAX_PLAYED_CARD
        self.__cdeck_free = MAX_PLAYED_CARD

        for i in range(len(self.__mydeck)):
            self.__mydeck[i].configure(image=self.__im)
            self.__cdeck[i].configure(image=self.__im)

        self.__my_ims = []

        for i in range(2):
            tmp = random.choice(list(self.__cards.keys()))
            self.__mypoints += self.__cards[tmp]
            self.__myim = PhotoImage(file=tmp)
            self.__my_ims.append(self.__myim)
            del self.__cards[tmp] # REMOVE USED CARDS FROM THE DECK

        self.__mydeck_free = MAX_PLAYED_CARD - 2 # käyttäjällä on 7 vapaata korttipaikkaa
        self.update_cards()

    def __pc_game_start(self):
        """
        Metodi aloittaa tietokoneen pelivuoron.
        :return: ei palauta mitään
        """
        self.__lock_gameButtons() # poistetaan kaikki painikkeet käytöstä
        self.__pc_ims = [] # alustetaan tietokoneen kortit

        for i in range(2):
            tmp = random.choice(list(self.__cards.keys()))
            self.__cpoints += self.__cards[tmp]
            self.__myim = PhotoImage(file=tmp)
            self.__pc_ims.append(self.__myim)
            del self.__cards[tmp] # REMOVE USED CARDS FROM THE DECK

        self.__cdeck_free = MAX_PLAYED_CARD - 2 # tietokoneella on 7 vapaata korttipaikkaa
        self.update_cards()

        while True:
            proceed = self.proceed_pc_game()
            self.update_cards()
            if proceed == True:
                break

        self.game_end()


    def proceed_pc_game(self):
        """
        Metodi jatkaa tietokoneen vuoroa, ensimmäisen jälkeen.
        :return: True/False. Jos True, niin metodin __pc_game_start vuoro päättyy
        """
        tm = random.choice(list([1,2,3])) # Valitaan satunnaisesti 1, 2 tai 3 sekuntia
        time.sleep(tm) # pysäytetään ohjelma valituksi ajaksi (kone "ajattelee", otetaanko seuraava kortti

        if self.__cpoints > 21:
            return True

        elif self.__cpoints == 21:
            return True

        # jos koneen pistemäärä on >= 18 ja < 21 ja on vapaita paikkoja
        elif self.__cpoints >= 18 and self.__cpoints < 21 and self.__cdeck_free != 0:
            # valitaan satunnaisesti nolla tai yksi
            risk = random.choice(list([0,1])) # Will the machine take a risk?
            # jos yksi, niin kone on ottanut riskin ottamalla seuraava kortti
            if risk:
                tmp = random.choice(list(self.__cards.keys()))
                self.__cpoints += self.__cards[tmp]
                self.__myim = PhotoImage(file=tmp)
                self.__pc_ims.append(self.__myim)
                del self.__cards[tmp]  # REMOVE USED CARDS FROM THE DECK
                self.__cdeck_free -= 1
                self.update_cards()
                if self.__cpoints > 21:
                    return True
                return False

            else:
                return True

        # jos koneen pistemäärä on vähemmän kuin 18, otetaan seuraava kortti epäilemättä
        elif self.__cpoints < 18 and self.__cdeck_free != 0:
            tmp = random.choice(list(self.__cards.keys()))
            self.__cpoints += self.__cards[tmp]
            self.__myim = PhotoImage(file=tmp)
            self.__pc_ims.append(self.__myim)
            del self.__cards[tmp]  # REMOVE USED CARDS FROM THE DECK
            self.__cdeck_free -= 1
            self.update_cards()
            if self.__cpoints > 21:
                return True
            return False


    def fill_card_deck(self,fname):
        """
        Metodi lukee tiedostosta "fname" korttikuvien nimet ja kortteja vastaavat pisteet.
        Jos jostain syystä lukeminen ei onnistu, ohjelma ilmoittaa epäonnistumisesta ja sulkeutuu
        :param fname: tiedosto, jossa ovat kortit ja pisteet
        :return:
        """
        try:
            with open(fname,"r") as f:
                for rivi in f:
                    temp = rivi.split(" ")
                    key = "giffit/" + temp[0]
                    value = int(temp[1])
                    self.__cards[key] = value
        except OSError:
            mb.showerror("ERROR!", "There is an error while reading the file")
            self.__window.destroy()

    def __get_me_more(self):
        """
        Metodi antaa lisää yhden kortin käyttäjälle. Jos vapaita paikkoja ei enää ole, ei tapahdu mitään.
        Jos käyttäjän pisteet ovat enemmän tai yhtäsuuri kuin 21, vuoro vaihtuu automaattisesti.
        :return:
        """
        if self.__mydeck_free == 0:
            return

        tmp = random.choice(list(self.__cards.keys()))
        self.__my_im = PhotoImage(file=tmp)
        self.__mypoints += self.__cards[tmp]
        self.__my_ims.append(self.__my_im)
        self.__mydeck_free -= 1
        self.update_cards()

        if self.__mypoints >= 21:
            self.__lock_gameButtons()
            Thread(target=self.__pc_game_start).start()

    def update_cards(self):
        # Päivittää kuvat ja pelipisteet pöydällä

        for i in range(9-self.__mydeck_free):
            self.__mydeck[i].configure(image=self.__my_ims[i])

        for i in range(9-self.__cdeck_free):
            self.__cdeck[i].configure(image=self.__pc_ims[i])

        lbl_string = "Player scores: " + str(self.__mypoints)
        self.__p_one_label.configure(text=lbl_string)
        lbl_string = "PC scores: " + str(self.__cpoints)
        self.__pc_label.configure(text=lbl_string)

    def __lock_gameButtons(self):
        # Poistaa käytästä kaikki painikkeet
        for i in range(4):
            self.__buttons[i].configure(state=DISABLED)

    def __release_gameButtons(self):
        # Vapauttaa kaikki painikkeet
        for i in range(4):
            self.__buttons[i].configure(state=NORMAL)

    def game_end(self):
        """
        Metodi vapauttaa "Close" ja "New game"-painikkeet ja määrittelee voittajan
        ilmoittaen msgboxilla.
        :return:
        """
        for i in range(2,4):
            self.__buttons[i].configure(state=NORMAL)
        if self.__mypoints > 21 or self.__cpoints > 21:
            if self.__mypoints > 21 and self.__cpoints <= 21:
                self.__winner = "PC won the game!"
            elif self.__mypoints <=21 and self.__cpoints > 21:
                self.__winner = "You won the game!"
            elif self.__mypoints > 21 and self.__cpoints > 21:
                self.__winner = "No one won the game!"
        elif self.__mypoints <= 21 and self.__cpoints <= 21:
            if self.__mypoints > self.__cpoints:
                self.__winner = "You won the game!"
            elif self.__mypoints == self.__cpoints:
                self.__winner = "No one won!"
            else:
                self.__winner = "PC won the game!"
        mb.showinfo("Winner!",self.__winner)


    def _close(self):
        self.__window.destroy()

    def start(self):
        self.__window.mainloop()


def main():
    ui = BJ()
    ui.start()

main()