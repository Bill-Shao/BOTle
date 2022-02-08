
def getWords():
    with open('wordleanswers.txt', 'r') as f:
        lines = f.readlines()
    lines = [lines[i].split("\t")[2] for i in range(1,len(lines))]
    return lines