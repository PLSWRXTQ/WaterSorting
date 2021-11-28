import random, pickle
from hashlib import new

lst = [
    ([[1, 1, 1], [1]], 4),
    ([[1, 1, 2], [2, 2, 2], [1, 1]], 4),
    ([[1, 2, 1, 2], [2, 1, 2, 1], []], 4),
    ([[1, 3, 2, 3], [1, 2, 3, 3], [1, 1, 2, 2], [], []], 4),
    ([[1, 4, 1, 2], [1, 2, 4, 3], [3, 4, 1, 3], [2, 3, 2, 4], [], []], 4),
    ([[1, 3, 4, 4], [1, 3, 2, 4], [2, 1, 3, 4], [1, 2, 2, 3], [], []], 4),
    ([[1, 5, 2, 3], [3, 5, 2, 1], [4, 1, 3, 2], [2, 4, 3, 1], [4, 4, 5, 5], [], []], 4),
    ([[1, 3, 4, 5], [2, 1, 5, 3], [3, 6, 5, 2], [3, 4, 5, 6], [1, 1, 2, 2], [4, 4, 6, 6], [], [], []], 4),
    ([[3, 6, 4, 7], [3, 2, 1, 5], [3, 3, 1, 7], [2, 2, 4, 5], [4, 4, 5, 5], [1, 2, 6, 7], [6, 7, 1, 6], [], []], 4),
    ([[2, 10, 9, 8], [3, 1, 5, 7], [4, 6, 9, 8], [4, 2, 7, 3], [5, 1, 10, 6], [9, 2, 4, 1], [3, 7, 6, 10], [5, 8, 5, 7], [9, 1, 2, 4], [3, 8, 10, 6], [], [], []], 4)
]

def read(uri):
    return pickle.load(open(uri, 'rb')) 

def getRandom(limit):
    l = []
    counting = [0 for _ in range(limit-1)]
    for _ in range(limit):
        t = []
        for _ in range(random.randint(0, limit-1)):
            n = random.randint(1, limit-1)
            if counting[n-1] < limit:
                t.append(n)
                counting[n-1] += 1
        l.append(t)
    return l

def getMD5(level_tuple):
    return new('md5', pickle.dumps(level_tuple)).hexdigest()