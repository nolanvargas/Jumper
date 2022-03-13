class Jumper: #Jumper class is the character and tracks its status

    def __init__(self):
        self._health = 4 # the health of the jumper
        self._jumper = { # this dictionary is so the jumper can be printed to the terminal
                        3: ' ___ ',
                        2: '/___\\',
                        1: '\\   /',
                        0: ' \\ / ',
                    'head': '  o  ',
                    'arms': ' /|\\ ',
                    'legs': ' / \\ ',
                    'gap': '',
                    'ground': '^^^^^'
                        }


    def update_health(self): # updates the health and the self._jumper dictionary
        self._health -= 1
        self._jumper.pop(self._health)   
        if self._health == 0: # when health is equal to 0 this changes the value in the dictionary so the person looks like they're dead
            self._jumper['head'] = '  x  '  
            
        
    def get_health(self): # gets the health and returns a boolean
        if self._health > 0:
            return True
        else:
            return False


    def get_jumper(self): # gets the jumper dictionary and returns it
        return list(self._jumper.values())
