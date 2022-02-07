import csv,codecs
from random import choice

def getData(filename):
    rows=[]
    with codecs.open(filename, 'r') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=' ')
        for row in csvreader:
            rows.append(row[0])
    return rows

def sortWords(words,maxDigits):
    wordsLengthSorted=[[] for i in range(maxDigits)]
    for word in words:
        index=len(word)-1
        if index<maxDigits:
            wordsLengthSorted[index].append(word) 
        else:
            pass
    return wordsLengthSorted

def bestGuess(wordList):
    wordLength=len(wordList[0])
    bestFreq=''
    for i in range(wordLength):
        freq=[0 for i in range(26)]
        for word in wordList:
            word=word.lower()
            char=word[i]
            index=ord(char)-96
            if index>0 and index<26:
                freq[index]+=1
            else:
                pass
        maxNum=0
        maxIndex=0
        for i in range(len(freq)):
            if freq[i]>maxNum:
                maxNum=freq[i]
                maxIndex=i
        bestFreq+=chr(maxIndex)
    scores=[]
    for word in wordList:
        score=0
        for i in range(wordLength):
            if word[i]==bestFreq[i]:
                score+=1
        scores.append(score)
    maxNum=0
    maxIndex=0
    for i in range(len(scores)):
        if scores[i]>maxNum:
            maxNum=scores[i]
            maxIndex=i
    return wordList[i]


def main():
    wordLength=int(input('Enter Word Length: '))
    possibleWords=sortedWords[wordLength-1]
    firstGuess=choice(possibleWords[0:10])
    '''
    The first guess is based on the most common word,
    or for more replayability it is based on a randomly 
    selected highly common word.

    The best guess on the other hand aims to guess a word such that,
    The letters of the word best match the most common letter possible for that spot,
    while taking care to consider that the word is still a real word.
    '''
    print(firstGuess)
    print(bestGuess(possibleWords))
    '''
    Please Note: Result format is 
    0 indicates no match
    1 indicates pseudo match
    2 indicates perfect match
    '''
    running=True
    while running:
        initialGuess=input('What was the initial guess? ')
        if initialGuess=='':
            running=False
            break
        resultGuess=input('What was the result? ')
        discardedChars=[]
        pseudoMatch=[]
        perfectMatch=[]
        for i in range(wordLength):
            if resultGuess[i]=='0':
                discardedChars.append(initialGuess[i])
            elif resultGuess[i]=='1':
                pseudoMatch.append((initialGuess[i],i))
            elif resultGuess[i]=='2':
                perfectMatch.append((initialGuess[i],i))
            else:
                '''
                Tiny easter egg for fun. 
                '''
                print('THOU ART A FOOL. GIVE THY LORD PROPER INPUT')

        discardedChars=list(set(discardedChars))
        print(discardedChars,pseudoMatch,perfectMatch)
        #Filter for empty characters
        updatedPossibleWords=[]
        for word in possibleWords:
            addWord=True
            for disChar in discardedChars:
                if disChar in word:
                    addWord=False
                    '''
                    I tried adding the optimization to skip 
                    checking for the rest of the characters
                    in case one of them triggers the flag.

                    While this should work, it would lead to 
                    unresolved bugs and thus at the time of writing,
                    this optimization is disabled.
                    '''
                #break
            '''
            I tried the optimization of skipping the 
            rest in case it has already been decided 
            that this word will be skipped. 

            However at the time of writing this produced 
            some unresolved bugs. Thus this optimization
            is disabled.
            '''
            #if addWord==True:
            if True:
                for pM,index in pseudoMatch:
                    if pM not in word:
                        addWord=False
                    elif word[index]==pM:
                        addWord=False
                    #break
            #if addWord==True:
            if True:
                for eM,index in perfectMatch:
                    if word[index]!=eM:
                        addWord=False
                    #break
            if addWord==True:
                updatedPossibleWords.append(word)
        possibleWords=updatedPossibleWords
        if len(possibleWords)<10:
            if len(possibleWords)==1:
                running=False
            else:
                print(possibleWords)
        else:
            print(possibleWords[0])
            print(bestGuess(possibleWords[0:10]))
        print(len(possibleWords))

words=getData('wikiWordList.txt')
sortedWords=sortWords(words,9)
main()
