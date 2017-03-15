#################################################################################
## Tron                                                                        ##
##                                                                             ##
## In the futuristic thriller, the protagonists ride bikes that leave infinite ##
## solid walls that could endanger other riders if they crash into them. As a  ##
## rider changes direction, their new coordinate is given in an array. Given   ##
## such an array of coordinates and a new coordinate representing the motorist,##
## determine whether the rider crashes and return a boolean. You may assume    ##
## the directional changes are not diagonally.                                 ##
##                                                                             ##
##     e.g. A = [(0, 0), (0, 1), (2, 1)]                                       ##
##          Rider = (1, 1) => True                                             ##
##          Rider = (2, 3) => False                                            ##
##                                                                             ##
#################################################################################

# Tron Crash
# Test whether a crash occurred (True) or the rider is safe (False)
# O(n) time and O(1) space
def tronCrash(coordinates, rider):
    for coord in range(len(coordinates) - 1):
        holdLeft = coordinates[coord]
        holdRight = coordinates[coord+1]
        
        if (holdLeft[0] is not holdRight[0] and holdLeft[0] > holdRight[0]) or \
            (holdLeft[1] is not holdRight[1] and holdLeft[1] > holdRight[1]):
            swap = holdLeft
            holdLeft = holdRight
            holdRight = swap
        
        # Python's comparators are pretty!
        if (holdLeft[0] <= rider[0] <= holdRight[0]) and \
            (holdLeft[1] <= rider[1] <= holdRight[1]):
            return True
            
    return False
    

def main():
    testCoords = [(0, 0), (0, 1), (2, 1)]
    rider = (1, 1)
    
    print "Testing Coordinates: " + str(testCoords) + "\nRider: " + str(rider)
    
    if tronCrash(testCoords, rider):
        print "Rider CRASHED\n"
    else:
        print "Rider SAFE\n"
        
    
    rider = (2, 3)
    
    print "Testing Coordinates: " + str(testCoords) + "\nRider: " + str(rider)
    
    if tronCrash(testCoords, rider):
        print "Rider CRASHED\n"
    else:
        print "Rider SAFE\n"
      
        
    rider = (1, 0)
    testCoords.append((2, -1))
    testCoords.append((0, -1))
    
    print "Testing Coordinates: " + str(testCoords) + "\nRider: " + str(rider)
    
    if tronCrash(testCoords, rider):
        print "Rider CRASHED\n"
    else:
        print "Rider SAFE\n"
        
    rider = (1, -1)
    print "Testing Coordinates: " + str(testCoords) + "\nRider: " + str(rider)
    
    if tronCrash(testCoords, rider):
        print "Rider CRASHED\n"
    else:
        print "Rider SAFE\n"
    

main()    