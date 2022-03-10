class Word:

    def __init__(self):
        #Open file, populate a list.
        with open("formatted_data.csv", "r") as file:
            self._words = file.readlines()[1:]
            print(self._words)

    def createEasy(self): #3-5 word length
        return self._filterList(3,5)

    def createNormal(self): #6-8 word length
        return self._filterList(6,8)

    def createHard(self): #9+ word length
        return self._filterList(9,99)

    def _filterList(self, minLength, maxLength):
        self.diff_list = []
        for item in self._words:
            if len(item[0]) >= minLength and len(item[0]) <= maxLength:
                self.diff_list.append(item[0])
        return self.diff_list