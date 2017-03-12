#################################################################################
## Major Studies                                                               ##
##                                                                             ##
## Every school has a set of requirements needed to fulfil a degree. Some      ##
## classes have dependencies that must be met before the class can be taken.   ##
## Given an input of a major, read in the data from the file formatted as:     ##
##     Class Name, Qualifies, Qualifies                                        ##
##     Class Name                                                              ##
## Where "Class Name" denotes a class, and "Qualifies" will be another Class   ##
## Name in the data set. You may assume that the data will not have impossible ##
## requisites, such as missing or cyclic references. The return will be a list ##
## of classes that the requester should take in order or an empty list.        ##
##                                                                             ##
##     e.g. Input: "Biology" with data set:                                    ##
##          Math 101, Math 181                                                 ##
##          Math 181, Biology 202                                              ##
##          Biology 202                                                        ##
##          Biology 101, Biology 202                                           ##
##                                                                             ##
##         Result: ['Biology 101', 'Math 101', 'Math 181', 'Biology 202']      ##
##          -OR-   ['Math 101', 'Biology 101', 'Math 181', 'Biology 202']      ##
##                                                                             ##
#################################################################################

import sys

# Class
# Class class for representing classes.
# But really, though, stores the title, classes this instance qualifies, and
# expands for a steps count for how many degrees calculated in sort below
class Class:
    
    def __init__(self, className):
        self.title = className
        self.requisites = []
        self.steps = 0
        
    # Less than
    # Overloaded operation for sorting
    def __lt__(self, right):
        if self.steps < right.steps:
            return True
        else:
            return False
        

# Program
# Graph holding class for the course requisites
class Program:
    
    # Constructor
    # Initializes the values from the given text file name
    # Writes the instances of the Class nodes
    def __init__(self, fileName):
        self.degree = fileName
        self.classes = {}
        
        values = []
        
        with open(fileName + ".txt", 'r') as file:
            values = file.read().strip().lower().split('\n')
            
        for each in values:
            schedule = each.split(',')
            
            for seq in schedule:
                lesson = Class(seq.strip().lower())
                self.classes[lesson.title] = lesson
            
        for each in values:
            schedule = each.split(',')
            hold = self.classes.get(schedule[0].strip().lower(), None)
            hold.requisites = []
            
            if hold is not None:
                schedule.pop(0)
                
                for req in schedule:
                    find = self.classes.get(req.strip().lower(), None)
                    
                    if find is not None:
                        find.steps += 1
                        hold.requisites.append(find)
                    else:
                        find = Class(req.strip().lower())
                        hold.requisites.append(find)
                
                hold.requisites = hold.requisites[:]
                self.classes[hold.title] = hold
            
    # Print
    # Prints the current set of classes in the listing
    def printProgram(self):
        print self.degree + ":"
        
        for key, value in self.classes.items():
            printString = str(key)
            
            for each in value.requisites:
                printString += " -> " + each.title
                
            print printString + '\n'
    
    # Sorts the classes by the pre-requisites
    # Initial weighting is performed a initialization, sorted, and then, 
    # topological sort by value as each is finished and found
    def sortClasses(self):
        values = list(self.classes.values())
        results = []
        
        while len(values) > 0:
            hold = values.pop(0)
            
            if hold.steps <= 0:
                results.append(hold)
                
                for each in hold.requisites:
                    each.steps -= 1
            else:
                values.append(hold)
                
        return results
        

def main():
    program = raw_input("What degree do you want to search? : ")
    program.strip().lower()
    
    program = Program(program)
    program.printProgram()

    order = program.sortClasses()
    
    for each in order:
        print each.title
        
main()
