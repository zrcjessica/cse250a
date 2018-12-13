import pandas as pd
from collections import Counter

WORD_COUNTS_FH = 'hw1_word_counts_05.txt'

### initialize
words_df = pd.read_table(WORD_COUNTS_FH, names=['words', 'counts'], sep='\s+')
WORDS_DICT = dict(zip(words_df.words, words_df.counts))
TOT_WORDS = words_df.counts.sum()
alphabet = dict(Counter(''.join(list(map(lambda x,y: ''.join([x]*y), words_df.words, words_df.counts)))))

### 1.9(a) ###
words_df['priors'] = words_df.counts.apply(lambda x: x*1.0/TOT_WORDS)
PRIORS_DICT = dict(zip(words_df.words, words_df.priors))
words_df = words_df.sort_values('priors').reset_index(drop=True)
mostFreq = list(words_df.tail(15).words)
leastFreq = list(words_df.head(14).words)
print('15 most frequent 5-letter words:')
for each in mostFreq:
	print each
print('14 least frequent 5-letter words:')
for each in leastFreq:
	print each

################# 
# corrDict: python dictionary representing correctly guessed letters in a word
# key: letter 
# value: list of key's position(s) in word
# incorrect guesses represented as list of strings

# checks if a word matches evidence for incorrect guesses
def matchIncorrect(incorrList, word):
    for letter in incorrList:
        if letter in word:
            return False
    return True

# checks if a word matches the correct evidence:
def matchCorrect(corrDict, word):
    correctLetters = corrDict.keys()
    for letter in correctLetters:
        positions = corrDict[letter]
        for pos in positions:
            if not word[pos] == letter:
                return False
    return True

# checks if letters in word are missing from dict of correctly guessed letters
def isMissingCorrect(corrDict, word):
    letters = list(word)
    for idx in xrange(0,len(letters)):
        ltr = letters[idx]
        if corrDict.has_key(ltr):
            posList = corrDict[ltr]
            if not idx in posList:
                return False
    return True

# checks if the evidence matched the current word checked
def checkEvidence(corrDict, incorrDict, word):
    isCorr = matchCorrect(corrDict, word)
    isIncorr = matchIncorrect(incorrDict, word)
    isMiss = isMissingCorrect(corrDict, word)

    if isCorr and isIncorr and isMiss:
        return True
    return False

def hangman(curLetter, corrDict, incorrList):
    letterProb = 0.0
    for word in WORDS_DICT.keys():
        wordLetters = list(word)
        corKeys = corrDict.keys()
        #only continue with the calculations if the word actually contains the letter
        if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corKeys:
            numEvidence = checkEvidence(corrDict,incorrList,word)
            if not numEvidence:
                continue
            numWcount = WORDS_DICT[word]
            denomCount = 0.0
            for again_words in WORDS_DICT.keys():
                tempDenom = checkEvidence(corrDict,incorrList,again_words)
                if not tempDenom:
                    continue
                tempDenomCount = WORDS_DICT[again_words]
                denomCount += tempDenomCount
            letterProb += numWcount/denomCount
    return letterProb

def filter(curLetter,corrDict,incorrList):
    sumWords = 0
    allwords = WORDS_DICT.keys()
    corrKeys = corrDict.keys()
    for wrd in allwords:
        numEvidence = checkEvidence(corrDict,incorrList,wrd)
        if numEvidence:
            sumWords += 1
        #if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corrKeys:
    return sumWords

# return best next guess l (bestGuess) and the probability it is correct (probCorr)
def goAlphabet(alphabet,corrDict,incorrList):
    abcLetters = alphabet.keys()
    probCorr = 0.0
    bestGuess = ''

    for k in xrange(0,len(abcLetters)):
        temp_prob = hangman(abcLetters[k],corrDict,incorrList)
        alphabet[abcLetters[k]]=temp_prob
        if temp_prob > probCorr:
            probCorr = temp_prob
            bestGuess = abcLetters[k]
    print [bestGuess, probCorr]


### Examples

# ex1Corr = {}
# ex1Corr['U'] = [1]
# ex1Incorr=['A','E','I','O','S']
# goAlphabet(alphabet,ex1Corr,ex1Incorr)

#ex2Corr = {}
#ex2Corr['D'] = [0]
#ex2Corr['I'] = [3]
#ex2Incorr = ['A']
#goAlphabet(alphabet,ex2Corr,ex2Incorr)

#ex3Corr = {}
#ex3Incorr = ['E','O']
#goAlphabet(alphabet,ex3Corr,ex3Incorr)

### Cases to fill out
# case1Corr = {}
# case1Incorr = []
# print 'correctly guessed'
# print case1Corr
# print 'incorrectly guessed'
# print case1Incorr
# goAlphabet(alphabet,case1Corr,case1Incorr)

# case2Corr = {}
# case2Incorr = ['E','A']
# print 'correctly guessed'
# print case2Corr
# print 'incorrectly guessed'
# print case2Incorr
# goAlphabet(alphabet,case2Corr,case2Incorr)

# case3Corr = {}
# case3Corr['A']=[0]
# case3Corr['S']=[4]
# case3Incorr = []
# print 'correctly guessed'
# print case3Corr
# print 'incorrectly guessed'
# print case3Incorr
# goAlphabet(alphabet,case3Corr,case3Incorr)

# case4Corr = {}
# case4Corr['A']=[0]
# case4Corr['S']=[4]
# case4Incorr = ['I']
# print 'correctly guessed'
# print case4Corr
# print 'incorrectly guessed'
# print case4Incorr
# goAlphabet(alphabet,case4Corr,case4Incorr)

case5Corr = {}
case5Corr['O']=[2]
case5Incorr = ['A','E','M','N','T']
print 'correctly guessed'
print case5Corr
print 'incorrectly guessed'
print case5Incorr
goAlphabet(alphabet,case5Corr,case5Incorr)

