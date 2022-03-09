from jumper.word import Word
from jumper.jumper import Jumper

class Director:

    def __init__(self):
        self.jumper = Jumper()
        self.word = Word()
        self.display_word = ["_"] * len(self.word)
        #["_" for i in self.word]
        self.difficulty = 0
        self.guesses = []
        self.is_playing = True

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

    
