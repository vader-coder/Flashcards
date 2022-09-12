import re, sys

def removeParentheses(text):
    return re.sub(r'\([^)]*\)', '', text)

def getEn(word):#for the "dor" one. 
    return word.replace("dor", "tor")


filename = "spanish/madrigal 1 or.txt"
if len(sys.argv) >= 2:
    filename = sys.argv[1]

direction = "es-en"
f = open(filename, "r")
words = f.read()
words = removeParentheses(words).replace("\n", " ").split()
last = len(words)-1
for i in range(last):
    words[i] = "el " + words[i] + " = " + words[i] + "\n"
words[last] += " = " + words[last]
words.insert(0, direction + "\n")
open(filename, "w").write(''.join(words))
