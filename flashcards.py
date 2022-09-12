#some import statements
#decide on type later.

from helper import query, guessLoop
from clueLanguage import ClueLanguage

files = {0:'fr/français 1.txt', 1:'fr/français 1 review.txt'}
fileToCollection = {}

def main():

    while True:
        print(files)
        strInput = input("give us a file number, a file path, or enter c to continue with the current one: ")
        fileName = strInput
        if strInput.isnumeric():
            number = int(strInput)
            fileName = files[number]
        collection = "x"
        if fileName in fileToCollection:
            collection = fileToCollection[fileName]
        else:
            collection = query(fileName)
            fileToCollection[fileName] = collection

        ans = "n"
        while ans != "y":
            print(
                f"Your clues will be in {collection.clueLanguage.getTargetLanguage()}.\nPress y to continue, n to switch and any other key to change your input file.")
            ans = input()
            if ans == "n":
                collection.switchOrder()
                continue

        guessLoop(collection)

        collection.reload()

main()
