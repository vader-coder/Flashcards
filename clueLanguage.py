class ClueLanguage():
    def __init__(self, language1, language2):
        self.target = language1
        self.other = language2
    
    def toggle(self):
        temp = self.target
        self.target = self.other
        self.other = temp

    def getTargetLanguage(self):
        return self.target
