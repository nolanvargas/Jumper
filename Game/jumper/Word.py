class word:
    def createEasy(self, wordCSV): #3-5 word length
        minLen = 3
        maxLen = 5
    def createNormal(self, wordCSV): #6-8 word length
        minLen = 6
        maxLen = 8
    def createHard(self, wordCSV): #9+ word length
        minLen = 9
        maxLen = 99

    def checkLength(self, item, minLen, maxLen): #used in map to collect proper length words.
        if len(item) >= minLen and len(item) <= maxLen:
            return item