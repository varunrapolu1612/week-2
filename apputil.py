import numpy as np

def ways(n):
    '''
    def ways(n):
    x=int(n//5)
    ways = list()
    for i in range(x+1):  
        ways.append((n-(5*i), i))
    return ways
    '''
    if n<0:
        return 0
    else:
        return (int(n//5) + 1)

def lowest_score(names, scores):
    # index of the lowest score
    min_index = np.argmin(scores)
    # Return a tuple (name, score)
    return (names[min_index])

def sort_names(names, scores):
    #sorting names and scores by sorted indices
    sorted_names = names[np.argsort(-scores)]
    sorted_scores = scores[np.argsort(-scores)]
    # Return list of (name, score) pairs
    return list(sorted_names)
