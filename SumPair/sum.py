################################################################################
## Sum Pairs                                                                  ##
##                                                                            ##
## Given an array of sorted integers and a total, find a pair in the data set ##
## that sums to the total value. Print the pair and return a boolean of found ##
## or not.                                                                    ##
##     e.g. A = [1, 2, 4, 5, 6] total = 8 => "2, 6" True                      ##
##          A = [-1, 7, 9] total = 5 => False                                 ##
##          A = [1, 2, 4, 4] total = 8 => "4, 4" True                         ##
##          A = [5] total = 5 => False (not a pair of values)                 ##
##                                                                            ##
##     1.) Write the function assuming the values are sorted.                 ##
##     2.) Write the function assuming the values are NOT sorted. How do they ##
##         differ?                                                            ##
##     3.) Suppose the values are unordered, but we are guaranteed that they  ##
##         are positive and have as many values as the total. i.e. The array  ##
##         is at least total-elements long.                                   ##
##                                                                            ##
################################################################################


# Sum the Pairs
# Assuming the values are sorted, the method uses two marching pointers to 
# compare the values at both ends of the array. If their total is too large,
# the higher pointer should move down and compare a lower value for the sum.
# Likewise, if the two pointers would be too small, the lower pointer needs
# to move up to a higher value.
# O(n) time, O(1) space
def sumPairs(values, total):
    if len(values) < 2:
        return False
        
    low = 0
    high = len(values) - 1
    
    while low < high:
        sumTotal = values[low] + values[high]
        
        if sumTotal == total:
            print str(values[low]) + " + " + str(values[high]) + " = " + str(total)
            return True
        elif sumTotal < total:
            low += 1
        else:
            high -= 1
            
    return False

# Sum Unsorted values
# In this implmentation, no guarantees are made about the ordering of the data
# and each must be compared for the complement. A scan of the list for each item
# could be performed, but at O(n^2), it is computationally heavy. This implementation
# cuts down the time complexity to O(n), but takes up additional O(n) space. Be
# sure to ask whether space or time is more valuable in this situation.
# O(n) time, O(n) space
def sumUnsorted(values, total):
    foundValues = set()
    
    if len(values) < 2:
        return False
        
    for value in values:
        complement = total - value
        
        if complement in foundValues:
            print str(complement) + " + " + str(value) + " = " + str(total)
            return True
        else:
            foundValues.add(value)
    
    return False
    
# Sum all Positive and Array Length as large as total
# Since we know the length of the elements in the array are at least as long as
# the target total, that allows us to use the array as a marker for values we 
# have already seen. For instance, if the total is 4 and we have 5 elements:
#     values = [3, 2, 2, 1, 4] total = 4
#     values[0] = 3, complement is 1, but 2 is positive => values [3, 2, 2, -1, 4]
#     values[1] = 2, complement 2 => values [3, 2, -2, -1, 4]
#     values[2] = 2, complement 2, and values[2] is negative! => print out "2 + 2 = 4"
#               and return True
# O(n) time, O(1) space
def sumAllPositives(values, total):
    if len(values) <= total and total < 2:
        return False
        
    for value in range(len(values)):
        complement = total - abs(values[value])
        
        if values[complement] < 0:
            print str(complement) + " + " + str(abs(value)) + " = " + str(total)
            return True
        else:
            if values[values[value]] >= 0:
                values[values[value]] *= -1
    
    return False


def main():
    A = [1, 2, 4, 5, 6]
    print "Input: " + str(A) + ", total = 8"
    sumPairs(A, 8)
    
    A = [-1, 7, 9]
    print "Input: " + str(A) + ", total = 5"
    if not sumPairs(A, 5):
        print "No pairs"
    
    A = [1, 2, 4, 4]
    print "Input: " + str(A) + ", total = 8"
    sumPairs(A, 8)
    
    A = [5]
    print "Input: " + str(A) + ", total = 5"
    if not sumPairs(A, 5):
        print "Not a pair of values"
        
    A = [7, 1, 3, 2, 4, 4]
    print "Input: " + str(A) + ", total = 8"
    sumUnsorted(A, 8)
    
    A = [18, -1, 2, 4, 3, 4]
    print "Input: " + str(A) + ", total = 8"
    sumUnsorted(A, 8)
    
    A = [7, 1, 3, 5, 7, 1, 2, 4, 4]
    print "Input: " + str(A) + ", total = 8"
    sumAllPositives(A, 8)


main()
