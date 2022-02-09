from unittest import result
from main import *
from utils import *

correctWord = "elder"

def getCombo(guess):
    combo = ""
    for i in range(len(guess)):
        if guess[i] == correctWord[i]:
            combo += "G"
        elif guess[i] in correctWord and guess[i] != correctWord[i]:
            combo += "Y"
        else:
            combo += "B"
    return combo

def runGame():
    guess = "crane"

    guessesLeft = 5

    while guessesLeft > 0:
        guess = guess.strip("\n")
        print("GUESS: " + guess + " LENGTH: " + str(len(guess)))
        comboIndex = comboToIndex(getCombo(guess))
        results = getNewDict(comboIndex,guess)
        changeDict(results)
        print(len(results))
        
        
        maxBit = 0
        for word in results:
            bit = (probDistribution(word))
            if bit > maxBit:
                maxBit = bit
                guess = word
        print("REMAINING WORDS:" + str(results))

        guessesLeft-=1

runGame()