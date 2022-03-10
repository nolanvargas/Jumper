class Jumper:

    def __innit__(self):
        self._jumper = { # this dictionary is so the jumper can be printed to the terminal
                        4: ' ___ ',
                        3: '/___\\',
                        2: '\\   /',
                        1: ' \\ / ',
                    'head': '  o  ',
                    'arms': ' /|\\ ',
                    'legs': ' / \\ '
                        }
        self._health = 4 # the health of the jumper


    def update_health(self): # updates the health and the self._jumper dictionary
        self._jumper.pop(self._health)
        self._health -= 1
        if self._health == 0: # when health is equal to 0 this changes the value in the dictionary so the person looks like they're dead
            self._jumper['head'] = 'x'


    def get_health(self): # gets the health and returns it
        return self._health