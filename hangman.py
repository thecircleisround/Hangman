from random import seed
from random import choice

class Settings():
    def __init__(self):
        self.gameactive = True
        self.chances = 10


class Words():
    def __init__(self):
        self.worddisplay = ""
        self.guesslist = []
    
    def pickword(self):
        while True:
            categories = ["sports", "musicians", "states"]

            print("Choose a category from the following list")
            for category in categories:
                print(category)
            category = input("> ")
            filename = (category + ".txt")
            try:
                f = open(filename, "r")
                words = f.read().splitlines()
                randomword = choice(words)
                return randomword
            except FileNotFoundError:
                print("Not a valid category")

def Hangman(): 
    def __init__(self):
        self.words = Words

def startgame(Settings):
    settings = Settings()
    words = Words()
    while True:
        word = words.pickword()
        displayword(settings, words, word)
        while settings.gameactive:
            userguess(settings, words, word)
            displayword(settings, words, word)
            updatestatus(settings, words, word)

        break


def displayword(settings, words, word):
    worddisplay = ""
    for p in word:
        if (p.lower() in words.guesslist or p == " "):
            worddisplay += p
        else:
            worddisplay += "_ "
    words.worddisplay = worddisplay
    print(words.worddisplay)
    print("Letters guessed so far " + str(words.guesslist))


def userguess(settings, words, word):
    userguess = input().lower()
    for i in userguess:
        words.guesslist.append(i)
    words.guesslist = list(set(words.guesslist))
    if userguess in word.lower():
        print("You got one!\n")
    else:
        print("Not in this word. Try again!")
        settings.chances -= 1
        print(str(settings.chances) + " trys remaining\n")


def updatestatus(settings, words, word):
    if words.worddisplay == word:
        print("You win!")
        settings.gameactive = False
    if settings.chances == 0:
        print("You lose!")
        print(settings.chances)
        print("The answer was: " + word)
        settings.gameactive = False


def playagain():
    playagain = input("Play again? (yes/no) ")
    if playagain == "yes":
        pass
    else:
        quit()


while True:
    startgame(Settings)
    playagain()


