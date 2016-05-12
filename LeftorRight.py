import argparse

leftHand = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
rightHand = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}

parser = argparse.ArgumentParser(
    description="Find words that can be typed with the left or right-hand. "
                "Makes for fast-typed passwords that are hard to guess from watching them typed.")
parser.add_argument("DICTIONARY", help="dictionary file to use")
parser.add_argument("LEFT", help="write left-handed words to file")
parser.add_argument("RIGHT", help="write right-handed words to file")

args = parser.parse_args()


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


dictionaryFileName = args.DICTIONARY
leftFileName = args.LEFT
rightFileName = args.RIGHT

dictionaryFile = open(dictionaryFileName, 'r')
trialWords = dictionaryFile.readlines()
dictionaryFile.close()

leftFile = open(leftFileName, 'w')
rightFile = open(rightFileName, 'w')

leftCount = 0
rightCount = 0
neitherCount = 0

for trialWord in trialWords:

    if leftCheck(trialWord, 0):
        leftCount += 1
        leftFile.write(trialWord)
    elif rightCheck(trialWord, 0):
        rightCount += 1
        rightFile.write(trialWord)
    else:
        neitherCount += 1

leftFile.close()
rightFile.close()

totalCount = neitherCount + rightCount + leftCount

print("Total Words: %d" % (totalCount))
print("Right Words: %d (%.3f%%)" % (rightCount, float(rightCount) / float(totalCount) * 100.0))
print("Left Words: %d (%.3f%%)" % (leftCount, float(leftCount) / float(totalCount) * 100.0))
print("Neither Words: %d (%.3f%%)" % (neitherCount, float(neitherCount) / float(totalCount) * 100.0))
