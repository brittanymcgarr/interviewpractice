################################################################################
## Find Anagrams                                                              ##
##                                                                            ##
## Given an array of strings and an array of various dictionary words, find   ##
## all anagrams in the dictionary words.                                      ##
##                                                                            ##
## e.g. A = ['dog', 'tab', 'cat']                                             ##
##      Dictionary = ['dog', 'god', 'good', 'bod', 'bat', 'tac', 'tack']      ##
##      => 'dog': 'dog', 'god'                                                ##
##      => 'tab': 'bat'                                                       ##
##      => 'cat': 'tac'                                                       ##
##                                                                            ##
################################################################################

# Find Anagrams
# Makes a hash dictionary of the sorted words from the dictionary with a list
# of words that match after sorting as the value. Great for Scrabble solving
# O(w*n*mlogm) time, O(n) space
# Where w = # words, n = words in dictionary, mlogm = sorting time for each word
# Lookup time after initial dictionary build:
# O(w*mlogm) time and O(1) lookup
def findAnagrams(words, dictionary):
    lookup = {}
    hold = []
    
    for value in dictionary:
        key = sorted(value)
        key = ''.join(key)
        
        hold = lookup.get(key, None)
        
        if hold == None:
            hold = []
        
        hold.append(value)
        lookup[key] = hold
    
    for word in words:
        key = sorted(word)
        key = ''.join(key)
        
        hold = lookup[key]
        
        if hold != None:
            print "\n" + word + ":"
    
            for result in hold:
                print result
        else:
            print word + " had no anagrams."
        

with open('words.txt', 'r') as file:
    dictionary = file.read().split('\n')
    
findAnagrams(['dog', 'cat', 'bat', 'wolf', 'cow', 'kiwi', 'ram', 'bug', 'duck', 'goose', 'asp', 'seal'], dictionary)
