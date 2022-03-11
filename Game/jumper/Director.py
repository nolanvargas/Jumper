from Game.jumper.Word import Word
from Game.jumper.Jumper import Jumper
from Game.jumper.Terminal_Service import terminalService

class Director:

    def __init__(self):
        self.jumper = Jumper()
        self.wordStart = Word()
        self.terminal = terminalService()
        #["_" for i in self.word]
        self.difficulty = ''
        self.guesses = []
        self.is_playing = True

    def start_game(self):
        self.prompt = "What difficulty would you like to play at? Easy, Normal, or Hard?"
        self.difficulty = self.terminal._getDifficultyInput(self.prompt).lower()
        self.update_difficulty(self.difficulty)
        
        if self.difficulty == "easy":
            self.word = Word.create_easy(self.wordStart)
        elif self.difficulty == "normal":
            self.word = Word.create_normal(self.wordStart)
        elif self.difficulty == "hard":
            self.word = Word.create_hard(self.wordStart)


        self.display_word = [' _ '] * len(self.word)
        print(self.word)

        while self.is_playing == True:
            print(''.join(self.display_word))
            self.get_input()
            self.update()

    def get_input(self):
        self.guess = self.terminal._getDifficultyInput('Guess a letter [a-z]: ').lower()

    def update_difficulty(self, difficulty):
        self.difficulty = difficulty

    def update(self):
        self.guesses.append(self.guess)
        word = list(self.word)
        if self.jumper.get_health:
            if self.guess in word:
                for i in range(len(word)):
                    if word[i] == self.guess:
                        self.display_word[i] = self.guess
            else:
                self.jumper.update_health()
        else: self.is_playing = False

    
