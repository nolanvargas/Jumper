class Jumper:

    def __innit__(self):
        self._jumper = {
                        4: ' ___ ',
                        3: '/___\\',
                        2: '\\   /',
                        1: ' \\ / ',
                    'head': '  o  ',
                    'arms': ' /|\\ ',
                    'legs': ' / \\ '
                        }
        self._health = 4


    def update_health(self):
        self._jumper.pop(self._health)
        self._health -= 1
        if self._health == 0:
            self._jumper['head'] = 'x'


    def get_health(self):
        return self._health