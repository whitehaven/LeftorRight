__author__ = 'WhiteHaven'

"""
Note that each word must include a newline, including the last one.
"""

import sys

leftHand = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
rightHand = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}


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


scriptName, dictionaryFileL, leftFileL, rightFileL = sys.argv

dictionaryFile = open(dictionaryFileL, 'r')

leftFile = open(leftFileL, 'w')
rightFile = open(rightFileL, 'w')

leftCount = 0
rightCount = 0
neitherCount = 0

trialWord = dictionaryFile.readline()

while trialWord != "":
    trialWord.lower()

    if leftCheck(trialWord, 0):
        leftCount += 1
        leftFile.write(trialWord)
    elif rightCheck(trialWord, 0):
        rightCount += 1
        rightFile.write(trialWord)
    else:
        neitherCount += 1

    trialWord = dictionaryFile.readline()

totalCount = neitherCount + rightCount + leftCount

print("Total Words: %d" % (totalCount))
print("Right Words: %d (%.3f%%)" % (rightCount, float(rightCount) / float(totalCount)))
print("Left Words: %d (%.3f%%)" % (leftCount, float(leftCount) / float(totalCount)))
print("Neither Words: %d (%.3f%%)" % (neitherCount, float(neitherCount) / float(totalCount)))
