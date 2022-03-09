class terminalService:
    #Handles terminal operations and provides input and outputs for the terminal.
    def letterPrompt(self, prompt): #Gets the input called from director. Prompt should be asking for a letter.
        return input(prompt)

    def getDifficultyInput(self, prompt): #Sets up the terminal input for difficulty selection.
        return input (prompt)

    def showJumper(self, jumperDict): #Gets the jumper to show the player how much longer he or she has until they lose.
        for item in jumperDict:
            print(item)