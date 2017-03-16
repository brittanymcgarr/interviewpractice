################################################################################
## Crossword Solver                                                           ##
## Hackerrank: https://www.hackerrank.com/challenges/crossword-puzzle         ##
##                                                                            ##
## Given a 10x10 input of characters where '-' denotes an empty space and '+' ##
## is a black space (no entry) and a list of words, return the appropriate    ##
## crossword solution.                                                        ##
##      e.g. Words = ['LONDON', 'DELHI', 'ICELAND', 'ANKARA']                 ##
##           Puzzle = [ '+-++++++++',                                         ##
##                      '+-++++++++',                                         ##
##                      '+-++++++++',                                         ##
##                      '+-----++++',                                         ##
##                      '+-+++-++++',                                         ##
##                      '+-+++-++++',                                         ##
##                      '+++++-++++',                                         ##
##                      '++------++',                                         ##
##                      '+++++-++++',                                         ##
##                      '+++++-++++' ]                                        ##
##                                                                            ##
##           Output = [ '+L++++++++',                                         ##
##                      '+O++++++++',                                         ##
##                      '+N++++++++',                                         ##
##                      '+DELHI++++',                                         ##
##                      '+O+++C++++',                                         ##
##                      '+N+++E++++',                                         ##
##                      '+++++L++++',                                         ##
##                      '++ANKARA++',                                         ##
##                      '+++++N++++',                                         ##
##                      '+++++D++++' ]                                        ##
##                                                                            ##
################################################################################


def solveCrossword(puzzle, words):
    if len(words) < 1:
        return puzzle
        
    wordsizes = {}
    
    for word in words:
        listed = wordsizes.get(len(word), [])
        listed.append(word)
        wordsizes[len(word)] = listed
        
    row = 0
    col = 0
    size = 0
    filled = False
    
    for rowCount in range(10):
        if '-' in puzzle[rowCount] and filled == False:
            count = 0
            start = -1
            end = -1
            
            for letter in range(10):
                if puzzle[rowCount][letter] is not '+':
                    count += 1
                    
                    if start < 0:
                        start = letter
                else:
                    end = letter - 1
                    
                if start >= 0 and end >= 0:
                    word = wordsizes.get(count, None)
                    
                    if word is not None:
                        word = word[0]
                        replace = list(puzzle[rowCount])
                        
                        for char in range(len(word)):
                            if puzzle[rowCount][start+char] == '-' or puzzle[rowCount][start+char] == word[char]:
                                replace[start+char] = word[char]
                            else:
                                start = -1
                                end = -1
                                count = 0
                                
                        if start >= 0:
                            filled = True
                            replace = "".join(replace)
                            puzzle[rowCount] = replace
                            words.remove(word)
                                
                            return solveCrossword(puzzle, words)
                    
    if filled == False:
        for colCount in range(10):
            colString = ''
            
            for rowCount in range(10):
                colString += str(puzzle[rowCount][colCount])
                
            if '-' in colString and filled == False:
                count = 0
                start = -1
                end = -1
                
                for char in range(10):
                    if colString[char] is not '+':
                        count += 1
                        
                        if start < 0:
                            start = char
                    else:
                        end = char - 1
                        
                    if start >= 0 and end >= 0:
                        word = wordsizes.get(count, None)
                        
                        if word is not None:
                            word = word[0]
                            replace = list(colString)
                            
                            for letter in range(count):
                                if colString[start+letter] == '-' or colString[start+letter] == word[letter]:
                                    replace[start+letter] = word[letter]
                                else:
                                    start = -1
                                    end = -1
                                    count = 0
                                    
                            if start >= 0:
                                filled = True
                                words.remove(word)
                                
                                for value in range(10):
                                    puzzle[value][colCount] = replace[value]
                                
                                return solveCrossword(puzzle, words)
    else:
        return puzzle
        
def main():
    testPuzzle = [  list('+-++++++++'),                                         
                    list('+-++++++++'),                                         
                    list('+-++++++++'),                                         
                    list('+-----++++'),                                         
                    list('+-+++-++++'),                                         
                    list('+-+++-++++'),                                         
                    list('+++++-++++'),                                         
                    list('++------++'),                                         
                    list('+++++-++++'),                                         
                    list('+++++-++++') ]  
                    
    testWords = ['LONDON', 'DELHI', 'ICELAND', 'ANKARA']
    
    result = solveCrossword(testPuzzle, testWords)
    
    print "Result:"
    
    for row in result:
        print str(row)

# STUB : Fix later
main()
