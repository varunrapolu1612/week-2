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
        return (int(n//2) + 1)

def lowest_score(names, scores):
    # indices that sort the scores in ascending order
    sorted_indices = np.argsort(scores)
    return names[sorted_indices]

def sort_names(names, scores):
    # indices that sort the scores in ascending order
    sorted_indices = np.argsort(scores)
    # Reverse for descending order
    sorted_indices = sorted_indices[::-1]
    return names[sorted_indices]
