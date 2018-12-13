import sys
from operator import itemgetter

file = open('word_counts_05.txt').readlines()

word_dict = {}
letter_dict = {}
alphabet = {}

#########################################
#a)

totalWords = 0

for line in file:
    temp = line.split()
    totalWords += int(temp[1])
    all_Letters = list(temp[0])
    for i in range(0,len(all_Letters)):
        if not alphabet.has_key(all_Letters[i]):
            alphabet[all_Letters[i]] = 0
    if not letter_dict.has_key(temp[0]):
        letter_dict[temp[0]] = all_Letters
    if not word_dict.has_key(temp[0]):
        word_dict[temp[0]] = int(temp[1])
    else:
        print(temp)

wd_list = word_dict.items()
words_only = word_dict.keys()
sortedDictList = sorted(wd_list, key = itemgetter(1))

bottom10 = sortedDictList[0:10]
top10 = sortedDictList[len(sortedDictList)-10:]

print top10
print bottom10
######################################################
testInput1_corr={}
testInput1_Incorr=[]
testInput1_Incorr.append('E')
testInput1_Incorr.append('O')
##
testInput2_corr={}
testInput2_Incorr=[]
testInput2_corr['D']=0
testInput2_corr['I']=3
##


####################################################

#corrdict format: letter and position(s) of the letter

#Checks if it matches the incorrect matching evidence
def isIncorrectMatch(incorrList,word):
    for letter in incorrList:
        if letter in word:
            return False

    return True

#checks if it matches the correct evidence:
def isCorrectMatch(corrDict,word):
    letterList = corrDict.keys()
    for letter in letterList:
        #pos can either have only one position or several, indicated by a list of positions
        pos = corrDict[letter]
        for i in range(0,len(pos)):
            if not word[pos[i]] == letter:
                return False

    return True

def isMissingCorrect(corrDict,word,letter_dict):
    lttrs = letter_dict[word]
    for l in range(0,5):
        lttr = lttrs[l]
        if corrDict.has_key(lttr):
            cpos = corrDict[lttr]
            if not l in cpos:
                return False

    return True

#checks if the evidence matched the current word checked
def checkEvidence(corrDict,incorrDict,word):
    isCorr = isCorrectMatch(corrDict,word)
    isIncorr = isIncorrectMatch(incorrDict,word)

    if isCorr and isIncorr:
        return True
    else:
        return False

    return

def checkEvidence2(corrDict,incorrDict,word):
    isCorr = isCorrectMatch(corrDict,word)
    isIncorr = isIncorrectMatch(incorrDict,word)
    isMiss = isMissingCorrect(corrDict,word,letter_dict)

    if isCorr and isIncorr and isMiss:
        return True
    else:
        return False

    return

#report the probability of seeing this word
def probWord(word,word_dict):
    occurances = float(word_dict[word])
    fraction = occurances/totalWords
    return fraction

#report the probability of seeing this word
def probWord2(word,word_dict,nrWords):
    occurances = float(word_dict[word])
    fraction = occurances/nrWords
    return fraction
#out = checkEvidence(testInput1_corr,testInput1_Incorr,'AARON')

def hangman(curLetter,corrDict,incorrList,word_dict):
    letterProb = 0.0
    for word in words_only:
        wordLetters = letter_dict[word]
        #occurInWord = wordLetters.count(curLetter)
        corKeys = corrDict.keys()
        #only continue with the calculations if the word actually contains the letter
        if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corKeys:
            numEvidence = checkEvidence(corrDict,incorrList,word)
            if not numEvidence:
                continue
            numWprob = probWord(word,word_dict)
            #denom = 0
            denomProb = 0
            for again_words in words_only:
                tempDenom = checkEvidence(corrDict,incorrList,again_words)
                if not tempDenom:
                    continue
                tempDenomProb = probWord(again_words,word_dict)
                #denom += tempDenom
                denomProb += tempDenomProb
            #numerator = numEvidence*numWprob
            #denominator = denom*denomProb
            letterProb += numWprob/denomProb

    return letterProb

def hangman6(curLetter,corrDict,incorrList,word_dict):
    letterProb = 0.0
    for word in words_only:
        wordLetters = letter_dict[word]
        #occurInWord = wordLetters.count(curLetter)
        corKeys = corrDict.keys()
        #only continue with the calculations if the word actually contains the letter
        if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corKeys:
            numEvidence = checkEvidence2(corrDict,incorrList,word)
            if not numEvidence:
                continue
            #numWprob = probWord(word,word_dict)
            numWcount = word_dict[word]
            #denom = 0
            denomCount = 0.0
            for again_words in words_only:
                tempDenom = checkEvidence2(corrDict,incorrList,again_words)
                if not tempDenom:
                    continue
                #tempDenomProb = probWord(again_words,word_dict)
                tempDenomCount = word_dict[again_words]
                #denom += tempDenom
                denomCount += tempDenomCount
            #numerator = numEvidence*numWprob
            #denominator = denom*denomProb
            letterProb += numWcount/denomCount

    return letterProb

def hangman4(curLetter,corrDict,incorrList,word_dict):
    letterProb = 0.0
    for word in words_only:
        wordLetters = letter_dict[word]
        #occurInWord = wordLetters.count(curLetter)
        corKeys = corrDict.keys()
        #only continue with the calculations if the word actually contains the letter
        if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corKeys:
            numEvidence = checkEvidence(corrDict,incorrList,word)
            if not numEvidence:
                continue
            #numWprob = probWord(word,word_dict)
            numWcount = word_dict[word]
            #denom = 0
            denomCount = 0.0
            for again_words in words_only:
                tempDenom = checkEvidence(corrDict,incorrList,again_words)
                if not tempDenom:
                    continue
                #tempDenomProb = probWord(again_words,word_dict)
                tempDenomCount = word_dict[again_words]
                #denom += tempDenom
                denomCount += tempDenomCount
            #numerator = numEvidence*numWprob
            #denominator = denom*denomProb
            letterProb += numWcount/denomCount

    return letterProb

def hangman5(curLetter,corrDict,incorrList,word_dict):
    letterProb = 0.0
    for word in words_only:
        wordLetters = letter_dict[word]
        #occurInWord = wordLetters.count(curLetter)
        corKeys = corrDict.keys()
        #only continue with the calculations if the word actually contains the letter
        if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corKeys:
            numEvidence = checkEvidence(corrDict,incorrList,word)
            if not numEvidence:
                continue
            #numWprob = probWord(word,word_dict)
            numWcount = word_dict[word]
            #denom = 0
            denomCount = 0.0
            for again_words in words_only:
                again_wordLetters = letter_dict[again_words]
                if curLetter in again_wordLetters:
                    tempDenom = checkEvidence(corrDict,incorrList,again_words)
                    if not tempDenom:
                        continue
                    #tempDenomProb = probWord(again_words,word_dict)
                    tempDenomCount = word_dict[again_words]
                    #denom += tempDenom
                    denomCount += tempDenomCount
            #numerator = numEvidence*numWprob
            #denominator = denom*denomProb
            letterProb += numWcount/denomCount

    return letterProb

def hangman3(curLetter,corrDict,incorrList,word_dict):
    letterProb = 0.0
    for word in words_only:
        wordLetters = letter_dict[word]
        #occurInWord = wordLetters.count(curLetter)
        corKeys = corrDict.keys()
        nrWords = filter(curLetter,corrDict,incorrList,word_dict)
        #only continue with the calculations if the word actually contains the letter
        if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corKeys:
            numEvidence = checkEvidence(corrDict,incorrList,word)
            if not numEvidence:
                continue
            numWprob = probWord2(word,word_dict,nrWords)
            #denom = 0
            denomProb = 0
            for again_words in words_only:
                tempDenom = checkEvidence(corrDict,incorrList,again_words)
                if not tempDenom:
                    continue
                tempDenomProb = probWord2(again_words,word_dict,nrWords)
                #denom += tempDenom
                denomProb += tempDenomProb
            #numerator = numEvidence*numWprob
            #denominator = denom*denomProb
            letterProb += numWprob/denomProb

    return letterProb

#incorrec, alphabet letter only applies to the first porbability statement
def hangman2(curLetter,corrDict,incorrList,word_dict):
    letterProb = 0.0
    for word in words_only:
        wordLetters = letter_dict[word]
        #occurInWord = wordLetters.count(curLetter)
        corKeys = corrDict.keys()
        #only continue with the calculations if the word actually contains the letter
        if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corKeys:
            numEvidence = checkEvidence(corrDict,incorrList,word)
            if not numEvidence:
                continue
            numWprob = probWord(word,word_dict)
            #denom = 0
            denomProb = 0
            for again_words in words_only:
                again_wordLetters = letter_dict[again_words]
                if curLetter in again_wordLetters:
                    tempDenom = checkEvidence(corrDict,incorrList,again_words)
                    if not tempDenom:
                        continue
                    tempDenomProb = probWord(again_words,word_dict)
                    #denom += tempDenom
                    denomProb += tempDenomProb
            #numerator = numEvidence*numWprob
            #denominator = denom*denomProb
            letterProb += numWprob/denomProb

    return letterProb

def filter(curLetter,corrDict,incorrList,word_dict):
    totalwords = 0
    allwords = word_dict.keys()
    corrKeys = corrDict.keys()
    for wrd in allwords:
        numEvidence = checkEvidence(corrDict,incorrList,wrd)
        if numEvidence:
            totalwords += 1
        #if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corrKeys:

    return totalwords

def goAlphabet(alphabet,corrDict,incorrList,word_dict):
    alphabet_Letters = alphabet.keys()

    highestProbLetter = 0.0
    highestProb = ''

    for k in range(0,len(alphabet_Letters)):
        temp_prob = hangman6(alphabet_Letters[k],corrDict,incorrList,word_dict)
        #prob = alphabet_Letters[alphabet_Letters[k]]*temp_prob
        alphabet[alphabet_Letters[k]]=temp_prob
        if temp_prob > highestProbLetter:
            highestProbLetter = temp_prob
            highestProb = alphabet_Letters[k]

    print alphabet
    return [highestProb,highestProbLetter]

#ex1Corr = {}
#ex1Corr['U'] = [1]
#ex1Incorr=['A','E','I','O','S']
#out = goAlphabet(alphabet,ex1Corr,ex1Incorr,word_dict)

#####
#ex2Corr = {}
#ex2Corr['D'] = [0]
#ex2Corr['I'] = [3]
#ex2Incorr = ['A']
#out = goAlphabet(alphabet,ex2Corr,ex2Incorr,word_dict)

#ex2Corr = {}
#ex2Corr['D'] = [0]
#ex2Corr['I'] = [3]
#ex2Incorr = []
#out = goAlphabet(alphabet,ex2Corr,ex2Incorr,word_dict)

#ex3Corr = {}
#ex3Incorr = ['E','O']
#out = goAlphabet(alphabet,ex3Corr,ex3Incorr,word_dict)



#######################3
#Real cases
#r1Corr = {}
#r1Incorr = []
#out = goAlphabet(alphabet,r1Corr,r1Incorr,word_dict)

#r2Corr = {}
#r2Incorr = ['E','A']
#out = goAlphabet(alphabet,r2Corr,r2Incorr,word_dict)

#r3Corr = {}
#r3Corr['A']=[0]
#r3Corr['S']=[4]
#r3Incorr = []
#out = goAlphabet(alphabet,r3Corr,r3Incorr,word_dict)

#r4Corr = {}
#r4Corr['A']=[0]
#r4Corr['S']=[4]
#r4Incorr = ['I']
#out = goAlphabet(alphabet,r4Corr,r4Incorr,word_dict)

r5Corr = {}
r5Corr['O']=[2]
r5Incorr = ['A','E','M','N','T']
out = goAlphabet(alphabet,r5Corr,r5Incorr,word_dict)

#test1Out = goAlphabet(alphabet,testInput1_corr,testInput1_Incorr,word_dict)

###
#test second statement
cdic ={}
#icL = []
#wrd = "ABOUT"

def testPart2(curLetter,corrDict,incorrList,word,word_dict,letter_dict):
    letterProb = 0.0
    wordLetters = letter_dict[word]
    occurInWord = wordLetters.count(curLetter)
    corKeys = corrDict.keys()
    #only continue with the calculations if the word actually contains the letter
    if curLetter in wordLetters and not curLetter in incorrList and not curLetter in corKeys:
        numEvidence = checkEvidence(corrDict,incorrList,word)
        #if not numEvidence:
        #    continue
        numWprob = probWord(word,word_dict)
        #denom = 0
        denomProb = 0
        for again_words in words_only:
            tempDenom = checkEvidence(corrDict,incorrList,again_words)
            if not tempDenom:
                continue
            tempDenomProb = probWord(again_words,word_dict)
            #denom += tempDenom
            denomProb += tempDenomProb
        #numerator = numEvidence*numWprob
        #denominator = denom*denomProb
        letterProb += occurInWord*numWprob/denomProb
        return letterProb
###
def testGoAlphabet(alphabet,corrDict,incorrList,word_dict,word,letter_dict):
    alphabet_Letters = alphabet.keys()

    highestProbLetter = 0.0
    highestProb = ''

    for k in range(0,len(alphabet_Letters)):
        temp_prob = testPart2(alphabet_Letters[k],corrDict,incorrList,word,word_dict,letter_dict)
        alphabet[alphabet_Letters[k]]=temp_prob
        if temp_prob > highestProbLetter:
            highestProbLetter = temp_prob
            highestProb = alphabet_Letters[k]


    return [highestProb,highestProbLetter]

#testGoAlphabet(alphabet,cdic,icL,word_dict,wrd,letter_dict)

###
#test second statement
#cdic ={}
#cdic['A']=[0]
#icL = []
#wrd = "ABOUT"
#testGoAlphabet(alphabet,cdic,icL,word_dict,wrd,letter_dict)

#test second statement
#cdic ={}
#cdic['A']=[0]
#icL = ['S']
#wrd = "ABOUT"
#testGoAlphabet(alphabet,cdic,icL,word_dict,wrd,letter_dict)

