

def convertListToString(lst):
    '''
    Takes a list as a parameter and returns all elements in the list as a String.
    '''

    funnyString = ""
    for i in range(len(lst)):
        funnyString = funnyString + lst[i]

    return funnyString