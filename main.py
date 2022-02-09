from numpy import allclose
import math
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from zmq import PROBE_ROUTER
from utils import *
from tqdm import tqdm
import ast

dictionary = getWords()
combos = allCombos()

def getProb(comboIndex,lines):
    return lines[comboIndex], len(lines[comboIndex]), len(lines[comboIndex])/len(dictionary) 

def getNewDict(comboIndex,word):
    f = open("C:\\Users\\Bill\\Desktop\\wordlebot\\storedDict\\" + word + ".txt")
    lines = f.read()
    lines = ast.literal_eval(lines)
    return lines[comboIndex]

def probDistribution(word):
    counts = []
    probs = []
    f = open("C:\\Users\\Bill\\Desktop\\wordlebot\\storedDict\\" + word.strip("\n") + ".txt")
    lines = f.read()
    lines = ast.literal_eval(lines)
    for i in range(len(combos)):
        a = getProb(i,lines)
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

def changeDict(newDict):
    global dictionary
    dictionary = newDict

