__author__ = 'WhiteHaven'

"""
Note that each word must include a newline, including the last one.
"""

import sys

leftHand = set()
leftHand.update(['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'])
rightHand = set()
rightHand.update(['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'])


def leftCheck(word, index):
    if word[index] == '\n':  # if we made it all the way here already, we have not hit a bad char yet, so true
        return True
    elif word[index] in leftHand:
        return leftCheck(word, index + 1)
    else:
        return False

def rightCheck(word, index):
    if word[index] == '\n':  # if we made it all the way here already, we have not hit a bad char yet, so true
        return True
    elif word[index] in rightHand:
        return rightCheck(word, index + 1)
    else:
        return False

print(sys.argv[0])
print(sys.argv[1])

dictionaryFile = open(sys.argv[1])

trialWord = dictionaryFile.readline()

while trialWord != "":
    trialWord.lower()

    print(trialWord,"   ",leftCheck(trialWord, 0),rightCheck(trialWord, 0))

    trialWord = dictionaryFile.readline()
