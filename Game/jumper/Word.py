class word:

    with open("formatted_data.csv", "r") as file:
        wordCSV = next(file)

    def __init__(self, wordCSV):
        #Open file, populate a list.
        self._words = []


    def createEasy(self): #3-5 word length
        return self._filterList(3,5)

    def createNormal(self): #6-8 word length
        return self._filterList(6,8)

    def createHard(self): #9+ word length
        return self._filterList(9,99)

    def _filterList(self, minLength, maxLength):
        list = []
        for item in self._words:
            if len(item[1]) >= minLength and len(item[1]) <= maxLength:
                list.append(item[1])
        return list