class Word:

    def __init__(self):
        self._wordsProcessed = []
        #Open file, populate a list.
        with open("jumper/formatted_data.csv", "r") as file:
            self._wordsRaw = file.readlines()[1:]
            for item in self._wordsRaw:
                self._wordsProcessed.append(item.split("," , 1))

    def createEasy(self): #3-5 word length
        return self._filterList(3,5)

    def createNormal(self): #6-8 word length
        return self._filterList(6,8)

    def createHard(self): #9+ word length
        return self._filterList(9,99)

    def _filterList(self, minLength, maxLength):
        self.diff_list = []
        for item in self._wordsProcessed:
            if len(item[0]) >= minLength and len(item[0]) <= maxLength:
                self.diff_list.append(item[0])
        return self.diff_list