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



def makeBoard(moves):
    #generates a board (integer of all 8's) of size/length equal to integer moves
    board = 0
    for i in range((moves)):
        board += 8*10**i

    return board

def digitCount(x):
    #returns integer equal to number of digits in x
    x = abs(x)
    if x == 0:
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
    if 0>dex or dex>9:
        print("ERROR: Index must be between 0 and 9 (inclusive). You entered:", dex)
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
