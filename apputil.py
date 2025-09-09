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
    # Convert inputs to NumPy arrays in case they are lists
    #names = np.array(names)
    #scores = np.array(scores)
    
    # Descending order
    sorted_indices = np.argsort(-scores)
    
    # Return only names in sorted order as a Python list
    return names[sorted_indices].tolist()
