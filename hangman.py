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

class Hangman():
    def __init__(self):
        self.words = Words()
        self.settings = Settings()
        
    def displayword(self, word):
        worddisplay = ""
        for p in word:
            if (p.lower() in self.words.guesslist or p == " "):
                worddisplay += p
            else:
                worddisplay += "_ "
            self.words.worddisplay = worddisplay
        print(self.words.worddisplay)
        print("Letters guessed so far " + str(self.words.guesslist))
    
    def userguess(self, word):
        userguess = input().lower()
        for i in userguess:
            self.words.guesslist.append(i)
        self.words.guesslist = list(set(self.words.guesslist))
        if userguess in word.lower():
            print("You got one!\n")
        else:
            print("Not in this word. Try again!")
            self.settings.chances -= 1
            print(str(self.settings.chances) + " trys remaining\n")
    
    def updatestatus(self, word):
        if self.words.worddisplay == word:
            print("You win!")
            self.settings.gameactive = False
        if self.settings.chances == 0:
            print("You lose!")
            print(self.settings.chances)
            print("The answer was: " + word)
            self.settings.gameactive = False
        
    def startgame(self):
        while True:
            word = self.words.pickword()
            self.displayword(word)
            while self.settings.gameactive:
                self.userguess(word)
                self.displayword(word)
                self.updatestatus(word)
            break
            
def playagain():
    playagain = input("Play again? (yes/no) ")
    if playagain == "yes":
        pass
    else:
        exit()


while True:
    hangman = Hangman()
    hangman.startgame()
    playagain()

