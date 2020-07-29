import numpy as np
import math

def rotateNumber(num):
    digiCount = math.floor(np.log10(num))
    lastDigit = num % 10
    restOfNum = num // 10

    return lastDigit*10**digiCount + restOfNum

def isPrime(n):
    if n < 4:
        return True

    for i in range(2,(math.ceil(np.sqrt(n))+1)):
        if n % i == 0:
            return False

    return True

def isCircularPrime(x):
    digiCount = math.floor(np.log10(x)) + 1

    for i in range(digiCount):
        if not isPrime(x):
            return False
        else:
            x = rotateNumber(x)

    return True

def nthCircularPrime(n):
    if (n < 0):
        print("ERROR: Negative input doesn't make sense. This function only takes positive integers as an argument")
        return -1
    elif n > 55:
        print("WARNING: This may take a very long time. If it's over 60 forget it (you entered:", n, ")")

    circPrimeCount = 0
    lastCircPrime = 1

    val = 2

    while(circPrimeCount < n):
        if isCircularPrime(val):
            circPrimeCount += 1
            lastCircPrime = val

        val += 1

    return lastCircPrime

assert(rotateNumber(12345) == 51234)
assert(rotateNumber(1) == 1)
assert(rotateNumber(15151) == 11515)

assert(isPrime(1) == True)
assert(isPrime(4) == False)
assert(isPrime(29) == True)

assert(isCircularPrime(3) == True)
assert(isCircularPrime(4) == False)
assert(isCircularPrime(37) == True)
assert(isCircularPrime(39) == False)

print("First 15 circular primes:")
for i in range(1,16):
    print(i,"-", nthCircularPrime(i))

print("\n")



def makeBoard(moves):
    #generates a board (integer of all 8's) of size/length equal to integer moves
    board = 0
    for i in range((moves)):
        board += 8*10**i

    return board

def digitCount(x):
    #returns integer equal to number of digits in x
    x = abs(x)
    if x // 10 == 0:
        #because log(0) is infinity and that makes python big mad
        return 1
    else:
        return math.ceil(np.log10(x))

def kthDigit(n,k):
    if (n < 0):
        n = abs(n)
    #returns the kth digit of n, with the 0th digit as the ones place
    return (n // 10**k) % 10

def replaceKthDigit(num, dex, val):
    #replaces kth digit of num with val
    if 0>val or val>9:
        print("ERROR: Value to be inserted must be between 0 and 9 (inclusive). You entered:", val)
    digits = digitCount(num)

    if dex >= digits:
        return val*10**dex + num
    else:
        output = 0
        for i in range(digits):
            if i == dex:
                output += val*10**i
            else:
                output += kthDigit(num, i)*10**i

        return output

def getLeftmostDigit(n):
    #returns the lefternmost digit of n
    digis = digitCount(n)

    if digis == 1:
        return n
    else:
        return (n // 10**(digis-1)) % 10

def clearLeftmostDigit(n):
    #makes lefternmost digit 0
    digis = digitCount(n)

    if digis == 1:
        return 0

    n = replaceKthDigit(n,(digis-1),0)

    return n

def makeMove(board,pos,move):
    if move != 1 and move != 2:
        return "move must be 1 or 2!"
    if pos > digitCount(board):
        return "offboard!"

    posDex = digitCount(board) - pos

    if kthDigit(board, posDex) != 8:
        return "occupied!"
    else:
        board = replaceKthDigit(board, posDex, move)

    return board

def isWin(board):
    #checks if the sequence '112' is somehwere in the board
    for i in range(2,digitCount(board)):
        if (board // 10**(i-2) % 1000) == 112:
            return True

    return False

def isFull(board):
    #check if the board is full (i.e. contains no 8's)
    for i in range(digitCount(board)):
        if kthDigit(board, i) == 8:
            return False
    return True

def play112(game):
    #function that drives the actual game
    board = makeBoard(getLeftmostDigit(game))
    game = clearLeftmostDigit(game)
    player = 1
    while game > 0:
        pos = getLeftmostDigit(game)
        game = clearLeftmostDigit(game)

        move =  getLeftmostDigit(game)
        game = clearLeftmostDigit(game)

        moveOutput = makeMove(board, pos, move)

        if isinstance(moveOutput, str):
            return str(board) + ": Player " + str(player) + ": " + moveOutput
        else:
            board = moveOutput

        if isWin(board):
            return str(board) + ": Player " + str(player) + " wins!"
        elif isFull(board):
            return str(board) + ": Tie!"

        if player == 1:
            player = 2
        else:
            player = 1

    return str(board) + ": Unfinished!"


def testHelperFuncs():
    print("Testing helper functions for play112...")
    assert(makeBoard(1) == 8)
    assert(makeBoard(2) == 88)
    assert(makeBoard(3) == 888)

    assert(digitCount(0) == 1)
    assert(digitCount(5) == digitCount(-5) == 1)
    assert(digitCount(42) == digitCount(-42) == 2)
    assert(digitCount(121) == digitCount(-121) == 3)

    assert(kthDigit(789, 0) == kthDigit(-789, 0) == 9)
    assert(kthDigit(789, 1) == kthDigit(-789, 1) == 8)
    assert(kthDigit(789, 2) == kthDigit(-789, 2) == 7)
    assert(kthDigit(789, 3) == kthDigit(-789, 3) == 0)
    assert(kthDigit(789, 4) == kthDigit(-789, 4) == 0)

    assert(replaceKthDigit(789, 0, 6) == 786)
    assert(replaceKthDigit(789, 1, 6) == 769)
    assert(replaceKthDigit(789, 2, 6) == 689)
    assert(replaceKthDigit(789, 3, 6) == 6789)
    assert(replaceKthDigit(789, 4, 6) == 60789)

    assert(getLeftmostDigit(7089) == 7)
    assert(getLeftmostDigit(89) == 8)
    assert(getLeftmostDigit(9) == 9)
    assert(getLeftmostDigit(0) == 0)

    assert(clearLeftmostDigit(789) == 89)
    assert(clearLeftmostDigit(89) == 9)
    assert(clearLeftmostDigit(9) == 0)
    assert(clearLeftmostDigit(0) == 0)
    assert(clearLeftmostDigit(60789) == 789)

    assert(makeMove(8, 1, 1) == 1)
    assert(makeMove(888888, 1, 1) == 188888)
    assert(makeMove(888888, 2, 1) == 818888)
    assert(makeMove(888888, 5, 2) == 888828)
    assert(makeMove(888888, 6, 2) == 888882)
    assert(makeMove(888888, 6, 3) == "move must be 1 or 2!")
    assert(makeMove(888888, 7, 1) == "offboard!")
    assert(makeMove(888881, 6, 1) == "occupied!")

    assert(isWin(888888) == False)
    assert(isWin(112888) == True)
    assert(isWin(811288) == True)
    assert(isWin(888112) == True)
    assert(isWin(211222) == True)
    assert(isWin(212212) == False)

    assert(isFull(888888) == False)
    assert(isFull(121888) == False)
    assert(isFull(812188) == False)
    assert(isFull(888121) == False)
    assert(isFull(212122) == True)
    assert(isFull(212212) == True)

    print("Passed!")

#testHelperFuncs()

def testPlay112():
    print("Testing play112()...")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

testPlay112()
