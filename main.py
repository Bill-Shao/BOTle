from numpy import allclose
import math
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from zmq import PROBE_ROUTER
from utils import *
from tqdm import tqdm

dictionary = getWords()
combos = allCombos()

def getProb(combo, word):
    validOptions = 0 
    result = []
    for choice in dictionary:
        valid = True
        #COMPARES THE WORD
        for i in range(5):
            if combo[i] == "G":
                if choice[i] != word[i]:
                    valid = False
                    break
            if combo[i] == "Y":
                if word[i] not in choice or choice[i] == word[i]:
                    valid = False
                    break 
            if combo[i] == "B": #black cuz grey green LMAO
                if word[i] in choice:
                    valid = False
                    break 
        #ADD OR NOT ADD 
        if valid:
            result.append(choice)
            validOptions +=1 

    return result,validOptions,validOptions/len(dictionary)


def probDistribution(word):
    counts = []
    probs = []
    for combo in combos:
        a = getProb(combo,word)
        counts.append(a[1])
        probs.append(a[2])
    bits = [bitTranslation(prob) for prob in probs]
    info = 0
    for i in range(len(probs)):
        info += bits[i] * probs[i]
    return info


def bitTranslation(prob):
    if prob == 0:
        return 0
    return -math.log(prob,2)


bitSig = 0
bestword = ""
for word in tqdm(dictionary):
    bit = probDistribution(word)
    if bit > bitSig:
        bitSig = bit
        bestword = word
print(bestword)

