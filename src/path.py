from email.mime import base
import fileHandling as fh
import general as g

obstacletxt = fh.getPathToCurrentDir("") + "obstacle.txt"
print(obstacletxt)

coordinates = {

}

baseCostOfMove = 10
costOfMoving = {
    0: baseCostOfMove,
    1: baseCostOfMove * 100,
}

def algo():
    while True:
        pass
        break


def convertCoordinateToInt(coordinates):

    '''
    <coordinate> 'x y'
    '''

    lst = str(coordinates).split(" ")
    return int(lst[0]), int(lst[1])

def convertObstacleToCoordinates():
    output = fh.readTXTFile(obstacletxt)

    global coordinates
    for y in range(len(output)):
        line = output[y]
        #print(line)
        tempList = line.split("\n")
        line = g.convertListToString(tempList)
        valueForEachSplit = line.split(" ")
        for x in range(len(valueForEachSplit)):
            coordinate = str(x) + " " + str(y)
            value = valueForEachSplit[x]
            coordinates[coordinate] = value

def getRelativeDirection(a, b):

    '''
    a should be one set of coordinates
    b should be different set of coordinates
    '''
    
    bX = convertCoordinateToInt(b)[0]
    bY = convertCoordinateToInt(b)[1]

    aX = convertCoordinateToInt(a)[0]
    aY = convertCoordinateToInt(a)[1]

    rightOfA = False
    leftOfA = False
    if bX > aX: #MEANS THAT b is to the right for a
        rightOfA = True
    elif bX < aX:
        leftOfA = True

    belowA = False
    aboveA = False

    if bY > aY: #MEANS THAT b is to the right for a
        belowA = True
    elif bY < aY:
        aboveA = True

    return aboveA, rightOfA, belowA, leftOfA

def getCoordinatesByValue(value):

    '''
    Returns coordinates in format "x y"
    '''

    for key in coordinates.keys():
        if coordinates.get(key) == value:
            return key

def getSurroundingValues(pos):
    global coordinates
    offSetList = [-1, 0, 1]

    BASEX = convertCoordinateToInt(pos)[0]
    BASEY = convertCoordinateToInt(pos)[1]

    surroundingValues = []    
    for y in range(len(offSetList)):
        for x in range(len(offSetList)):
            try:
                #print("heri")
                xpos = BASEX + offSetList[x]
                ypos = BASEY + offSetList[y]
                #print(offSetList[x], offSetList[y])
                coords = str(xpos) + " " + str(ypos)
                #print(coords, result)
                surroundingValues.append(coordinates.get(coords))
            except:
                print("error")
                pass

    return surroundingValues

convertObstacleToCoordinates() # MUST BE RUN FIRST
getSurroundingValues(getCoordinatesByValue("X"))