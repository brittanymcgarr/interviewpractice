################################################################################
## Dominator                                                                  ##
##                                                                            ##
## A dominator is an integer (positive) that occurs more than 1/2 n times for ##
## a given set of data. Given an array of integers, find the dominator of the ##
## array and print the value. Return -1 if no dominator is present.           ##
##    e.g. A = [1, 2, 3, 1, 1, 1] => 1                                        ##
##                                                                            ##
##    1.) Do this in O(n) time and up to O(n) space for any positive value.   ##
##    2.) Do this in O(n) time and up to O(1) space                           ##
##                                                                            ##
################################################################################


# Dominator
# This implementation uses the values of the stack as a counting hash and
# increments their values as each is encountered on the array. The final
# tallies are then compared against the half-total number of elements
# O(n) time, O(n) space
def dominator(values):
    valueDict = {}
    length = len(values)
    
    for index in xrange(length):
        hold = valueDict.get(values[index], None)
        
        if hold is not None:
            hold += 1
        else:
            hold = 1
            
        valueDict[values[index]] = hold
    
    maxCount = 0
    valueFound = -1
    
    for key, value in valueDict.items():
        if value > maxCount:
            maxCount = value
            valueFound = key
    
    if maxCount > (length / 2):
        return valueFound
    else:
        return -1


# Dominator Pseudo Stack
# This implementation makes note that the top of the stack should match the
# dominator, if one is present. If the top of the stack does not match, both
# values should be popped. A value that survives the stack is a candidate
# for a dominator. The candidate is then checked by counting against the list
# O(2n) => O(n) time, O(1) space by approximating the top of the stack
def dominatorStack(values):
    length = len(values)
    stack = 0
    
    for index in xrange(length):
        if stack == 0:
            stack += 1
            top = values[index]
        else:
            if top != values[index]:
                stack -= 1
            else:
                stack += 1
    
    candidate = -1
    leader = -1
    count = 0
    
    if stack > 0:
        candidate = top
    
    for index in xrange(length):
        if values[index] == candidate:
            count += 1
        
    if count > (length / 2):
        leader = candidate
        
    return leader


# Easy Dominator passes
test = [1, 2, 3, 2, 1, 1, 1]
testString = ""

print "Test case 1: "

for value in test:
    testString += str(value) + ', '

print str(testString)
print "Found dominator (1): " + str(dominator(test))
print "Found dominator (2): " + str(dominatorStack(test)) + '\n'


test = [1, 2, 1, 1, 2, 2, 2, 2, 3, 3, 2, 2]
testString = ""

print "Test case 2: "

for value in test:
    testString += str(value) + ', '

print str(testString)
    
print "Found dominator (1): " + str(dominator(test))
print "Found dominator (2): " + str(dominatorStack(test)) + '\n'

# Dominator fail
test = [1, 2, 1, 1, 2, 2, 3, 3, 3, 3, 3, 2, 2]
testString = ""

print "Test case 2: "

for value in test:
    testString += str(value) + ', '

print str(testString)
    
print "Found dominator (1): " + str(dominator(test))
print "Found dominator (2): " + str(dominatorStack(test)) + '\n'