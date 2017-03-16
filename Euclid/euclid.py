#################################################################################
## Euclid's Algorithm                                                          ##
##                                                                             ##
## Because what algorithm practice repo is complete without it? Euclidean      ##
## Greatest Common Divisor (GCD) algorithm is considered the "first" algorithm ##
## Given two integers, find their GCD.                                         ##
##     e.g. 595, 225 => 5                                                      ##
##                                                                             ##
#################################################################################


def euclidGCD(first, second):
    a = first
    b = second
    c = a % b
    
    while c is not 0:
        if a < b:
            swap = a
            a = b
            b = swap
        
        c = a % b
        
        if c is not 0:
            a = b
            b = c
            
    return b
    

def main():
    a = 595
    b = 225
    
    result = euclidGCD(a, b)
    
    print "Inputs: " + str(a) + ", " + str(b)
    print "Result: " + str(result)
    
    a = 512
    b = 220
    result = euclidGCD(a, b)
    
    print "Inputs: " + str(a) + ", " + str(b)
    print "Result: " + str(result)
    
    a = 139
    b = 139 * 4
    result = euclidGCD(a, b)
    
    print "Inputs: " + str(a) + ", " + str(b)
    print "Result: " + str(result)
    
main()