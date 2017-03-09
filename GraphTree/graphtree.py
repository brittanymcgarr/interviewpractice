#################################################################################
## Graph Tree Lowest Cost                                                      ##
##                                                                             ##
## Given a directed, acyclic and weighted graph as illustrated below, find the ##
## lowest cost from the origin node to ANY child. Each node has at most two    ##
## children labeled left and right.                                            ##
##     e.g.   1                                                                ##
##           / \        Result: 15 (1, 3, 5, 6)                                ##
##          2   3                                                              ##
##         / \ / \                                                             ##
##        8   4   5                                                            ##
##       / \ / \ / \                                                           ##
##      9  10   9   6                                                          ##
##                                                                             ##
#################################################################################

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        
       
# Find the Min Cost
# Find the minimum cost of reaching any leaf node on the given graph
# O(n^sqrt(n)) time, space
def findMinCost(root):
    paths = []
    minPath = 1000000
    
    if root is None:
        return -1
        
    paths.append((root, 0))
    
    while len(paths) > 0:
        holdNode = paths[0][0]
        holdCost = paths[0][1]
        
        if holdNode.left is None and holdNode.right is None:
            if minPath > holdCost + holdNode.data:
                minPath = holdCost + holdNode.data
        else:
            if holdNode.left is not None:
                paths.append((holdNode.left, holdCost + holdNode.data))
            if holdNode.right is not None:
                paths.append((holdNode.right, holdCost + holdNode.data))
        
        paths.pop(0)

    return minPath
    

def main():
    root = Node(1)
    
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(8)
    root.left.right = Node(4)
    root.right.left = root.left.right
    root.right.right = Node(5)
    root.left.left.left = Node(9)
    root.left.left.right = Node(10)
    root.left.right.left = root.left.left.right
    root.left.right.right = Node(9)
    root.right.right.left = root.left.right.right
    root.right.right.right = Node(6)
    
    print "Found Min Path: " + str(findMinCost(root))

main()
