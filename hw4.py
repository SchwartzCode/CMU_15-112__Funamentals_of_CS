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

print(bestScrabbleScore(wordDict2, letterScoreDict, ['a', 'b', 'c', 'd']))



# Problem 4

def getVal(input, localVars, args):
    try:
        input = int(input)
        print('ay')
        return input
    except:
        if input[0] == 'L':
            return localVars[ int(input[1:]) ]
        elif input[0] == 'A':
            return args[ int(input[1:]) ]
        else:
            return null

def solveExpression(relation, input1, input2, localVars, args):

    val1 = getVal(input1, localVars, args)
    val2 = getVal(input2, localVars, args)

    if relation == '-':
        return val1 - val2
    elif relation == '+':
        return val1 + val2
    else:
        return null

def runSimpleProgram(program, args):
    localVars = [ ]
    lines = program.split("\n")

    counter = 0
    i = 0
    while i <len(lines):
        lines[i] = lines[i].strip()
        if lines[i][0] != '!':
            items = lines[i].split(" ")
            print(i, items)
            if items[0][0] == 'L':
                index = int(items[0][1:])
                while (index+1) > len(localVars):
                    localVars.append(0)
                print(localVars, index)
                if len(items) == 4:
                    localVars[index] = solveExpression(items[1], items[2], items[3], localVars, args)
                else:
                    localVars[index] = getVal(items[1], localVars, args)
                print("Local Var assignment: L", items[0][1:])
                print("Val gotten: ", localVars[index])
            elif items[0] == "JMP":
                key = items[1] + ':'
                print(key)
                for j in range(len(lines)):
                    if lines[j].strip() == key:
                        print("aooga", j)
                        i=j
            elif items[0] == "JMP+" and getVal(items[1], localVars, args) > 0:
                key = items[2] + ':'
                print("JMP+ SEARCH..", key)
                for j in range(len(lines)):
                    print("JMP+ ", j, lines[j].strip())
                    if lines[j].strip() == key:
                        print("JMP FOUND")
                        i=j
            elif items[0] == "JMP0" and getVal(items[1], localVars, args) == 0:
                key = items[2] + ':'
                for j in range(len(lines)):
                    if lines[j].strip() == key:
                        i=j
            elif items[0] == "RTN":
                print("RETURN: ", getVal(items[1], localVars, args))
                return getVal(items[1], localVars, args)
        i += 1
        counter += 1
        if counter > 1000:
            print("!!! loop limit !!!")
            break

prog = """  ! aaa
 bb c dd
 moustache:
  L1 - A0 A1
ccccc asd gsfgsdf
JMP0 L1 moustache
RTN L1"""
args = [-5,5.1]


testieboy = [0, 0, 0]
testieboy.append(0)
testieboy[3] = 'potato'

print(testieboy)

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""

    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    print("part 2")
    print(runSimpleProgram(sumToN, [5]), '== 1+2+3+4+5', '===============')
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")
testRunSimpleProgram()
