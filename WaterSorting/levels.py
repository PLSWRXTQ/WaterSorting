import random, pickle

lst = [
    ([[1,3,2,3],[1,2,3,3],[1,1,2,2],[],[]], 4),
    ([[1,3,4,4],[1,3,2,4],[2,1,3,4],[1,2,2,3],[],[]], 4)
]

def read(uri):
    return pickle.load(open(uri)) 

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