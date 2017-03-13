################################################################################
## Heap                                                                       ##
##                                                                            ##
## Implement a max heap using an array. Include insert and remove functions.  ##
## Insert should leave the root and subtrees as max heaps of their children.  ##
## Remove should return the top value on the heap and ensure the max heap     ##
## integrity is preserved.                                                    ##
##                                                                            ##
##     e.g. Inserting values: 5, 3, 7, 2, 4                                   ##
##                      7                                                     ##
##                     / \                                                    ##
##                    4   5                                                   ##
##                   / \                                                      ##
##                  2   3                                                     ##
##          After Remove: return 7                                            ##
##                      5                                                     ##
##                     / \                                                    ##
##                    4   3                                                   ##
##                   /                                                        ##
##                  2                                                         ##
##                                                                            ##
################################################################################

from random import randint


class Heap:
    
    def __init__(self):
        self.data = []
    
    # Heapify
    # Heaps up the last set item until max heap structure is updated
    def heapify(self):
        index = len(self.data) - 1
        
        while index / 2 >= 0 and self.data[index] > self.data[index / 2]:
            swap = self.data[index]
            self.data[index] = self.data[index / 2]
            self.data[index / 2] = swap
            index = index / 2
            
    # Reheapify
    # Reheaps the structure from the root down
    def reheapify(self, index):
        large = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self.data) and self.data[index] < self.data[left]:
            large = left
            
        if right < len(self.data) and self.data[large] < self.data[right]:
            large = right
            
        if large is not index:
            swap = self.data[large]
            self.data[large] = self.data[index]
            self.data[index] = swap
            self.reheapify(large)
    
    # Insert
    # Insert the value into the max heap and call the heapify helper
    def insert(self, value):
        self.data.append(value)
        self.heapify()
        
    # Remove
    # Returns the max (root) value in the heap or a None value if no values
    # are present. Then, reheapifies the structure
    def remove(self):
        if len(self.data) > 0:
            hold = self.data[0]
            self.data[0] = self.data[-1]
            self.data.pop(-1)
            self.reheapify(0)
            return hold
        else:
            return None


def main():
    heap = Heap()
    count = 0
    
    while count < 10:
        count += 1
        heap.insert(randint(0, 100))
        print str(heap.data)

    removeList = []
    
    while len(heap.data) > 0:
        removeList.append(heap.remove())
    
    removeList = removeList[::-1]
    
    print "Sorted: " + str(removeList)


main()