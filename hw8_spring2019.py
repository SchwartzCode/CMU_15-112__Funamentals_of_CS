import matplotlib.pyplot as plt
import numpy as np
import timeit

# this function swaps the first and last elements of a list
#   time complexity: O(N)
def slow1(lst): # N is the length of the list lst
    assert(len(lst) >= 2) # O(1)
    a = lst.pop()         # O(1)
    b = lst.pop(0)        # O(N)
    lst.insert(0, a)      # O(N)
    lst.append(b)         # O(1)

    return lst

# time complexity: O(1)
def quick1(lst):
    assert(len(lst) >= 2) # O(1)
    tmp = lst[-1]         # O(1)
    lst[-1] = lst[0]      # O(1)
    lst[0] = tmp          # O(1)

    return lst            # O(1)




# Counts the number of unique entries in a list
#   time complexity: O(N^2)
def slow2(lst): # N is the length of the list lst
    counter = 0                     # O(1)
    for i in range(len(lst)):       # O(N)
        if lst[i] not in lst[:i]:     # worst case O(N), average case O(N)
            counter += 1              # O(1)
    return counter                  # O(1)

# time complexity: between O(N) and O(N^2), closer to O(N)
def quick2(lst):
    counter = 0                # O(1)
    seen = set()               # O(1)
    for x in lst:              # O(N)
        if x not in seen:        # worst case O(N), average case O(1)
            seen.add(x)          # O(1)
            counter += 1       # O(1)
    return counter             # O(1)


# finds the most commonly used lowercase letter in a string and returns it (if no lower case letters then it returns "")
# time complexity: O(N^2)
import string
def slow3(s): # N is the length of the string s
    maxLetter = ""                                              # O(1)
    maxCount = 0                                                # O(1)
    for c in s:                                                 # O(N)
        for letter in string.ascii_lowercase:                      # O(1)
            if c == letter:                                        # O(1)
                if s.count(c) > maxCount or \
                   s.count(c) == maxCount and c < maxLetter:       # O(N)
                    maxCount = s.count(c)                          # O(N)
                    maxLetter = c                                  # O(1)
    return maxLetter                                            # O(1)

# time complexity: O(N)
def quick3(s):
    maxLetter = ""                          # O(1)
    maxCount = 0                            # O(1)

    lettys = np.zeros(26)                   # O(1)

    for c in s:                             # O(N)
        if c in string.ascii_lowercase:         # O(1)
            lettys[ord(c) - 97] += 1            # O(1)

    for i in range(len(lettys)):            # O(1)
        if lettys[i] > maxCount:                # O(1)
            maxCount = lettys[i]                # O(1)
            maxLetter = chr(i + 97)             # O(1)

    return maxLetter                        #O(1)


# time complexity: O(N^2)
def slow4(a, b): # a and b are lists with the same length N
    n = len(a)                      # O(1)
    assert(n == len(b))             # O(1)
    result = abs(a[0] - b[0])       # O(1)
    for c in a:                     # O(N)
        for d in b:                     # O(N)
            delta = abs(c - d)              # O(1)
            if (delta > result):            # O(1)
                result = delta              # O(1)
    return result                   # O(1)



"""
# tried to do a manual big O estimate
times = [ ]
n_vals = [ ]

for i in range(5,20):
    test = np.arange(0, 100*i)
    n_vals.append(len(test))
    test = test.tolist()

    max = 0
    for j in range(10000):
        start = time.time()
        slow1(test)
        end = time.time()
        if (end-start) > max:
            max = end-start


    times.append(max)

plt.plot(n_vals, times)
plt.show()
"""

# Making sure my functions work the same as the intial function
tester = [1, 2, 3, 4]
tester2 = [1, 2, 3, 1, 3, 5, 6, 7, 3]
tester3 = 'HEY pp BABYYYYYY give me thaT penelope'
assert(slow1(tester.copy()) == quick1(tester.copy()))
assert(slow2(tester2.copy()) == quick2(tester2.copy()))
assert(slow3(tester3) == quick3(tester3))
