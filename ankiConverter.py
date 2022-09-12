#save in anki

#ankiConverter.py "filename" "es"
lang = "es"#fr

def reverseLanguages(lang):
    lang = lang.replace(" ", "").replace("\n", "").split("to")
    return lang[1] + "-" + lang[0] + ", "#"\uff1a"

def formatLang(lang):
    lang = lang.replace(" ", "").replace("\n", "").split("to")
    return lang[0] + "-" + lang[1] + ", "#"\uff1a"

def convertFile(filename):
    f = open(filename, "r")
    lines = f.readlines()#readlines, probably want to split it and make two files that go both ways. 
    reversed = list([])
    languages = lines.pop(0)
    last = len(lines)-1
    for i in range(len(lines)):#replace = w/ ";"
        line = lines[i]
        entry = line.split("=")
        switched = entry[1].replace("\n", "") + " ; " + entry[0]
        if i != last:
            switched += "\n"
        lines[i] = entry[0] + ";" + entry[1]
        reversed.append(switched)
    
    filename = filename.replace(lang+"/", "")
    fname1 = f"anki/{lang}/{formatLang(languages)}{filename}"
    fname2 = f"anki/{lang}/{reverseLanguages(languages)}{filename}"
    #"anki/" + reverseLanguages(languages) + filename
    open(fname1, "w").write(''.join(lines))
    open(fname2, "w").write(''.join(reversed))

convertFile(f"{lang}/madrigal 1 al.txt")
"""
import os
dirname = os.getcwd()
for files in os.listdir(dirname):
    if files.endswith((".txt")):
        print(files)
        convertFile(files)
"""