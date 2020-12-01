from random import choice
import ui
from time import sleep

reset = False

def chooseword(userentry, showword):
    choiceconfirmed = False
    word = hangman.words.pickword(userentry, showword)
    hangman.words.word = word
    if word is not None: 
        hangman.displayword(word, showword)
        hangman.settings.gameactive = True


def userentry(sender):
    userentry = sender.superview['userentry']
    showword = sender.superview['showword']
    userentry.end_editing()
    if userentry.text == "":
        pass
    else: 
        if hangman.settings.gameactive != True:
            chooseword(userentry, showword)
            userentry.text = ""
            userentry.begin_editing()
        else:
            word = hangman.words.word
            hangman.userguess(word, userentry, showword)
            hangman.displayword(word, showword)
            hangman.updatestatus(word, showword)
            userentry.text = ""
    userentry.begin_editing()  

def button_tapped(sender):
    sender.superview['submit'].text = "submit"
    userentry(sender)


view = ui.load_view('load_ui')


class Settings():
    def __init__(self):
        self.gameactive = False
        self.chances = 10


class Words():
    def __init__(self):
        self.worddisplay = ""
        self.word = ""
        self.guesslist = []
        self.showword = view['showword']

    def showcategories(self):
        categories = ["sports", "musicians", "states"]
        self.showword.text = "Choose a category from the following list"
        for category in categories:
            self.showword.text += "\n " + category

    def pickword(self, userentry, showword):
        filename = (userentry.text.lower() + ".txt")
        try:
            f = open(filename, "r")
            words = f.read().splitlines()
            randomword = choice(words)
            return randomword
        except FileNotFoundError:
            pass

class Hangman():
    def __init__(self):
        self.newgame()

    def displayword(self, word, showword):
        worddisplay = ""

        for p in word:
            if (p.lower() in self.words.guesslist or p == " "):
                worddisplay += p
            else:
                worddisplay += "_ "
            self.words.worddisplay = worddisplay
        # print("Letters guessed so far " + str(self.words.guesslist))
        showword.text = worddisplay

    def userguess(self, word, userentry, showword):
        for i in userentry.text:
            self.words.guesslist.append(i)
        self.words.guesslist = list(set(self.words.guesslist))
        if userentry.text in word.lower():
            #print("You got one!\n")
            pass
        else:
            #print("Not in this word. Try again!")
            self.settings.chances -= len(userentry.text)
            #print(str(self.settings.chances) + " trys remaining\n")

    def updatestatus(self, word, showword):
        if self.words.worddisplay == word:
            showword.text = word
            #showword.text = "You Win! Play again?"
            self.settings.gameactive = False
            self.newgame()

        if self.settings.chances <= 0:
            showword.text = "You lose!"
            #showword.text = "The answer was: " + word
            self.settings.gameactive = False
            self.newgame()
            
    def newgame(self): 
        self.settings = Settings()
        self.words = Words()
        self.words.showcategories()

    def playagain(userentry,showword):
        showword.text = "Play again?" 
        if userentry == "yes":
            self.newgame()
        else:
            quit()


view.present('sheet')



hangman = Hangman() 

#hangman.startgame()
#playagain()

