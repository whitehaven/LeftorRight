__author__ = 'WhiteHaven'

import sys

leftHand = set()
leftHand.update(['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b'])
rightHand = set()
rightHand.update(['y','u','i','o','p','h','j','k','l','n','m'])

print (sys.argv[0])
print (sys.argv[1])

dictionaryFile = open(sys.argv[1])

trialWord = dictionaryFile.readline()

trialWord.lower()

for letter in trialWord:
    print(letter)
    if letter in leftHand:
        print("Left Hand Letter")
    elif letter in rightHand:
        print("Right Hand Letter")
