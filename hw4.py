import itertools
from itertools import combinations, chain, permutations

# Problems 1 and 2
def nonDestructiveRotateList(list):
    new_list = [ list[-1] ] + list[:-1]

    return new_list

def destructiveRotateList(list):
    lastElem = list.pop()
    list.insert(0, lastElem)
    return list

test = [1,2,3,4]
assert(nonDestructiveRotateList(test) == [4,1,2,3])
assert(test == [1,2,3,4])
assert(destructiveRotateList(test) == [4,1,2,3])
assert(test == [4,1,2,3])

# Problem 3
def getScore(word, letterScores):
    score = 0
    for letter in word:
        score += letterScores[letter]
    return score

def bestScrabbleScore(dict, letterScores, hand):
    #initialize values
    bestWord = ''
    for letter in hand:
        bestWord += letter
    if bestWord in dict:
        bestScore = dict[bestWord]
    else:
        bestScore = 0

    output = [bestWord, bestScore]

    handCount = len(hand)
    #test = list(powerset(hand))
    #print(test)
    for i in range(1,handCount+1):
        combos = list(set(itertools.combinations(hand, i)))

        for combo in combos:
            permutations = list(itertools.permutations(combo))
            for perm in permutations:
                tmp = ''
                for letter in perm:
                    tmp += letter
                if tmp in dict:
                    score = getScore(tmp, letterScores)
                    if score > bestScore:
                        bestScore = score
                        bestWord = tmp
                        output = [bestWord, bestScore]
                    elif score == bestScore:
                        output = [output, [tmp, bestScore]]

    return output

letterScoreDict = {
    "a" : 1,
    "b" : 3,
    "c" : 3,
    "d" : 2,
    "e" : 1,
    "f" : 4,
    "g" : 2,
    "h" : 4,
    "i" : 1,
    "j" : 8,
    "k" : 5,
    "l" : 1,
    "m" : 3,
    "n" : 1,
    "o" : 1,
    "p" : 3,
    "q" : 10,
    "r" : 1,
    "s" : 1,
    "t" : 1,
    "u" : 1,
    "v" : 4,
    "w" : 4,
    "x" : 8,
    "y" : 4,
    "z" : 10
}

#wordDict2 is a big list of words I found online, wordDict is user-defined as seen below
fpath = r'C:\Users\jonbs\Documents\JonathanStuff\CMU_Stuff\words.txt'
wordDict2 = [ ]
with open(fpath, 'r') as file:
    for line in file:
        line = line.rstrip("\n")
        wordDict2.append(line)

wordDict = ['bad', 'ad', 'ab', 'dab', 'a', 'b', 'c']

print(bestScrabbleScore(wordDict2, letterScoreDict, ['a', 'b', 'c', 'd', 'e', 'j']))
assert(bestScrabbleScore(wordDict, letterScoreDict, ['a', 'b', 'c']) == ['ab', 4] )
assert(bestScrabbleScore(wordDict, letterScoreDict, ['a', 'b', 'c', 'd']) == [['bad',6], ['dab',6]] )
