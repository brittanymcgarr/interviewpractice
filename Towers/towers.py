################################################################################
## Towers of Hanoi                                                            ##
##                                                                            ##
## The classic recursion puzzle. The goal of the game is to move all the      ##
## discs of size 1-n from the left peg to the right with a center peg as the  ##
## inbetween. Smaller discs must be over larger discs. i.e. A disc of size 3  ##
## cannot be on a disc of size 2 but may be on a greater size. Given n discs  ##
## of 1-n, find the least moves to win the game.                              ##
##                                                                            ##
################################################################################

def hanoi(discs, frompeg, topeg, auxpeg, moves):
    if discs > 0:
        moves[0] += 1
        hanoi(discs - 1, frompeg, auxpeg, topeg, moves)
        
        if len(frompeg) > 0:
            topeg.append(frompeg.pop(-1))
        
        hanoi(discs - 1, auxpeg, topeg, frompeg, moves)

def main():
    A = []
    B = []
    C = []
    moves = [0]
    discs = 21
    
    while discs > 20 or discs < 1:
        discs = input("Enter 1-20 discs: ")
        
    A = range(discs, 0, -1)

    print "The stacks: "
    print "A: " + str(A)
    print "B: " + str(B)
    print "C: " + str(C)
    
    hanoi(discs, A, C, B, moves)
    print "Result: " + str(moves[0]) + " moves."
    print "The stacks: "
    print "A: " + str(A)
    print "B: " + str(B)
    print "C: " + str(C)
    
    
main()