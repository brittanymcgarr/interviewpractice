################################################################################
## Longest Common Subsequence                                                 ##
##                                                                            ##
## Given a pair of strings, X and Y, find the length of the longest, common   ##
## subsequence of the two. The ordering does not have to be strictly adjacent.##
##    e.g. X = "ABCDEFABACDDCE"                                               ##
##         Y = "ABDCE" => 5 ("ABDCE")                                         ##
##         Y = "CBDADC" => 5 ("BDADC")                                        ##
##         Y = "FGFHD" => 2 ("FD")                                            ##
##                                                                            ##
################################################################################

import copy


def LCS(X, Y):
    xsize = len(X)
    ysize = len(Y)
    
    table = []
    
    for row in range(0, xsize+1):
        column = []
        
        for col in range(0, ysize+1):
            column.append(0)
            
        table.append(copy.deepcopy(column))
        
    for x in xrange(xsize-1, -1, -1):
        for y in xrange(ysize-1, -1, -1):
            if X[x] == Y[y]:
                table[x][y] = table[x+1][y+1] + 1
            
            if table[x+1][y] > table[x][y]:
                table[x][y] = table[x+1][y]
            
            if table[x][y+1] > table[x][y]:
                table[x][y] = table[x][y+1]
    
    return table[0][0]
    
    
X = "ABCDEFABACDDCE"
Y = "ABDCE"

print "X: " + X
print "Y: " + Y
print "Result: " + str(LCS(X, Y)) + "\n"

Y = "CBDADC"
print "X: " + X
print "Y: " + Y
print "Result: " + str(LCS(X, Y)) + "\n"

Y = "FGFHD"
print "X: " + X
print "Y: " + Y
print "Result: " + str(LCS(X, Y)) + "\n"