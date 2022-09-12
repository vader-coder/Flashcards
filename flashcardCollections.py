import copy, random
from clueLanguage import ClueLanguage

class DictCollection:

    def __init__(self):
        self.dict = {}
        self.languageNameMap = {"fr": "French", "en": "English", "es": "Spanish"}

    def setLanguageMapping(self, str):
        wordList = str.split(" ")# should be only 3 words.
        self.clueLanguage = ClueLanguage(self.languageNameMap[wordList[0]], self.languageNameMap[wordList[2]])

    def load(self, fileName):
        f = open(fileName, "r", encoding="utf-8")
        lines = f.readlines()
        dict = {}
        print(lines[0])
        self.setLanguageMapping(lines[0].rstrip())
        for line in lines:
            if '=' in line:
                array = line.split(' = ')
                dict[array[0]] = array[1]
        self.dict = dict
        self.createInitialBackup()

    def createInitialBackup(self):
        self.backup = copy.deepcopy(self.dict)

    def switchOrder(self):
        self.dict = dict((y, x) for x, y in self.dict.items())
        self.clueLanguage.toggle()

    #when runs out of items
    def reload(self):
        self.dict = self.backup
        self.backup = copy.deepcopy(self.dict)

    def getRandomEntry(self):
        clue, answer = random.choice(list(self.dict.items()))
        del self.dict[clue]
        return clue, answer

    def add(self, clue, answer):
        self.dict[clue] = answer

    def isNotEmpty(self):
        if self.dict:
            return True
        else:
            return False
