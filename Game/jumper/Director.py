from Game.jumper.Word import Word
from Game.jumper.Jumper import Jumper
from Game.jumper.Terminal_Service import terminalService

class Director:

    def __init__(self):
        self.jumper = Jumper()
        self.wordStart = Word()
        self.terminal = terminalService()
        #["_" for i in self.word]
        self._difficulty = ''
        self.guesses = []
        self.is_playing = True

    def start_game(self):
        self.prompt = "What difficulty would you like to play at (Easy, Normal, or Hard): "
        self._difficulty = self.terminal._getDifficultyInput(self.prompt).lower()
        self.update_difficulty(self.difficulty)
        
        if self._difficulty == "easy":
            self.word = Word.create_easy(self.wordStart)
        elif self._difficulty == "normal":
            self.word = Word.create_normal(self.wordStart)
        elif self._difficulty == "hard":
            self.word = Word.create_hard(self.wordStart)


        self.display_word = [' _ '] * len(self.word)

        while self.is_playing == True:
            self.health = self.jumper.get_health()
            if self.health == True:
                print(''.join(self.display_word))
                print()
                jumper_list = self.jumper.get_jumper()
                for item in jumper_list:
                    print(item)
                print()
                self.get_input()
                self.update()
                if ' _ ' not in self.display_word:
                    self.is_playing = False
            else: self.is_playing = False
        if ' _ ' not in self.display_word:
            print()
            print(f'You guessed it! The word was {self.word}')
            
        else:
            dead_jumper = self.jumper.get_jumper()
            for item in dead_jumper:
                print(item)
            print(f'Game Over. The word was {self.word}')
    def get_input(self):
        self.guess = self.terminal._getDifficultyInput('Guess a letter [a-z]: ').lower()

    def update_difficulty(self, difficulty):
        self._difficulty = difficulty

    def update(self):
        self.guesses.append(self.guess)
        word = list(self.word)
        if self.health == True:
            if self.guess in word:
                for i in range(len(word)):
                    if word[i] == self.guess:
                        self.display_word[i] = self.guess
            else:
                self.jumper.update_health()
        else: 
            self.is_playing = False

    
