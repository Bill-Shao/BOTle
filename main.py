from dictionary import *
dictionary = getWords()



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
            if combo[i] == "Y":
                if word[i] not in choice or choice[i] == word[i]:
                    valid = False 
            if combo[i] == "B": #black cuz grey green LMAO
                if word[i] in choice:
                    valid = False 
        #ADD OR NOT ADD 
        if valid:
            result.append(choice)
            validOptions +=1 

    return result,validOptions,validOptions/len(dictionary)


print(getProb("BYBBB", "weary")[1])