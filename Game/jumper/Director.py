from game.jumper.word import Word
from game.jumper.jumper import Jumper
from game.jumper.terminal_Service import terminalService

class Director:

    def __init__(self):
        self.jumper = Jumper()
        self.wordStart = Word()
        #["_" for i in self.word]
        self.difficulty = 0
        self.guesses = []
        self.is_playing = True

    def start_game(self):
        self.prompt = "What difficulty would you like to play at? Easy, Normal, or Hard?"
        self.difficulty = terminalService._getDifficultyInput(self, self.prompt).lower()
        self.update_difficulty(self.difficulty)
        
        if self.difficulty == "easy":
            self.word = Word.create_easy(self.wordStart)
        elif self.difficulty == "normal":
            self.word = Word.create_normal(self.wordStart)
        elif self.difficulty == "hard":
            self.word = Word.create_hard(self.wordStart)


        self.display_word = ["_"] * len(self.word)
        self.update()

        while self.is_playing == True:
            self.update()

    def update_difficulty(self, difficulty):
        self.difficulty = difficulty

    def update(self, guess):
        while self.is_playing:
            self.guesses.append(guess)
            word = list(self.word)
            new_guess = ()
            if self.jumper.get_health() > 0 and (guess in self.guesses):
                if guess in word:
                    
                    pass
                else:
                    self.jumper.update_health()
            else: self.is_playing = False

    
