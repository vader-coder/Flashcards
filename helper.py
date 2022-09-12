from flashcardCollections import DictCollection

def query(fileName):
    collection = DictCollection()
    collection.load(fileName)
    return collection


def guessLoop(collection):
    review = DictCollection()
    reviewLater = False
    while collection.isNotEmpty():
        clue, answer = collection.getRandomEntry()
        print(f"clue: {clue}")
        guess = input("enter guess: ")
        print(guess)
        print(f"answer: {answer}")
        if not(guess in answer):
            ans = input("Enter y to review this word later: ")
            print(ans)
            if ans == "y" or ans == "Y":
                review.add(clue, answer)
                print("we will review the word later")
                reviewLater = True
            else:
                print("we won't bring up that word again.")
    print("checking if we need to review")
    if reviewLater == True:
        print("we have words to review")
        guessLoop(review)
    else:
        print("no more words to review")
