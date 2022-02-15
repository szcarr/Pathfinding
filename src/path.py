import fileHandling as fh
import general as g

obstacletxt = fh.getPathToCurrentDir("") + "obstacle.txt"
print(obstacletxt)
coordinates = {

}

def convertCoordinateToInt(coordinates):
    '''
    <coordinate> 'x y'
    '''

    lst = str(coordinates).split(" ")
    return lst[0], lst[1]

def convertObstacleToCoordinates():
    output = fh.readTXTFile(obstacletxt)

    global coordinates
    for y in range(len(output)):
        line = output[y]
        print(line)
        tempList = line.split("\n")
        line = g.convertListToString(tempList)
        valueForEachSplit = line.split(" ")
        for x in range(len(valueForEachSplit)):
            coordinate = str(x) + " " + str(y)
            value = valueForEachSplit[x]
            coordinates[coordinate] = value

def getRelativeDirection(a, b):

    '''
    a should be 
    '''
    
    if b > a:
        pass




def getLocationByValue(value):
    convertObstacleToCoordinates()
    for key in coordinates.keys():
        if coordinates.get(key) == value:
            return key


print(getLocationByValue("Y"))