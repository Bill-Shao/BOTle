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
    guess = guess.strip("\n")
    guessesLeft = 1

    while guessesLeft > 0:
        comboIndex = comboToIndex(getCombo(guess))
        results = getNewDict(comboIndex,guess)

        print(len(results))

        changeDict(results)
        maxBit = 0
        
        for word in tqdm(results):
            bit = (probDistribution(word))
            if bit > maxBit:
                maxBit = bit
                guess = word
        print(guess)

        guessesLeft-=1

runGame()