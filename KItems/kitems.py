################################################################################
## K-Items                                                                    ##
##                                                                            ##
## Given an input array of items, find the K-most frequently occuring items.  ##
##     e.g. A = [1, 2, 3, 1, 1, 2, 3, 2, 9, 9, 1, 9, 9, 9, 8, 7] and k = 2    ##
##            => [9, 1]                                                       ##
##                                                                            ##
################################################################################


def kItems(inputs, k):
    if len(inputs) <= k:
        return list(set(inputs))
        
    frequencies = {}
    
    for value in inputs:
        hold = frequencies.get(value, None)
        
        if hold == None:
            hold = 1
        else:
            hold += 1
            
        frequencies[value] = hold
        
    maxVal = 0
    
    for key, value in frequencies.items():
        if value > maxVal:
            maxVal = value
            
    hashLengths = [ [] for count in range(maxVal + 1) ]
    
    for key, value in frequencies.items():
        hashLengths[value].append(key)
    
    index = maxVal
    count = 0
    results = []
    
    while count < k and index >= 0:
        if hashLengths[index] is not []:
            while len(hashLengths[index]) > 0:
                results.append(hashLengths[index][0])
                hashLengths[index].pop(0)
                count += 1
            
            index -= 1
    
    return results
    
    
def main():
    inputs = [1, 2, 3, 1, 1, 2, 3, 2, 9, 9, 1, 9, 9, 9, 8, 7]
    print "First Test for k = 2: " + str(inputs)
    results = kItems(inputs, 2)
    print "Results: " + str(results)
    
    print "Second Test for k = 3: " + str(inputs)
    results = kItems(inputs, 3)
    print "Results: " + str(results)
    
main()
