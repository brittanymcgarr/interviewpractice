#################################################################################
## Kevin Bacon Game                                                            ##
##                                                                             ##    
## Kevin Bacon is an actor in many films. As a result of his fame, many actors ##
## play a game where they try to figure out the fewest connections between     ##
## cast members to Kevin Bacon.                                                ##
##                                                                             ##    
## e.g. Harrison Ford's "Bacon Number" is 2:                                   ##
##      Harrison Ford and Karen Allen appeared in Raiders of the Lost Ark.     ##
##      Karen Allen and Kevin Bacon appeared in Animal House.                  ##
##                                                                             ##            
## (You can type "Bacon Number X" where X is the actor's name into Google.)    ##
##                                                                             ##    
## Given a list of movies with the full cast names, create a data structure to ##
## store an actor's past cast members and find their Bacon Number. Bacon's     ##
## own Bacon Number is zero, and -1 indicates there are no listed connections  ##
## in the data set.                                                            ##
##                                                                             ##
#################################################################################

import copy


BACON = "Kevin Bacon"

class Actor:

    # Constructor with actor name
    def __init__(self, nameIN):
        self.name = nameIN
        self.casts = {}
        self.baconNumber = -1
        self.baconPath = []
    
    # Print Bacon Path
    # Examines the current Bacon Number of the actor and prints the
    # Bacon Path that has been found for the actor along with movies.
    def printBaconPath(self):
        if self.baconNumber < 0:
            print "\n" + self.name + " has no connection to Kevin Bacon listed.\n"
        elif self.baconNumber == 0:
            print self.name + " IS Kevin Bacon."
        else:
            print "\n" + self.name + "\'s Bacon Number is " + str(self.baconNumber) + ":\n"
            
            linkname = self.name
            
            for actor, movie in self.baconPath[::-1]:
                print linkname + " and " + actor + " appeared in " + movie + "."
                linkname = actor

    # Add Movie
    # Takes the title as a key for the Actor and adds the list of cast Actors
    # as the value
    def addMovie(self, movie, cast):
        if self in cast:
            self.casts[movie] = cast

    # Find Bacon
    # Uses a Breadth-first search to find Kevin Bacon from the given casts
    # Because Python is pass by reference (-ish), other Actors who have already
    # called this should be able to give their own Bacon Number and path, if
    # present
    def findBacon(self):
        # Handle the man, himself
        if self.name == BACON:
            self.baconNumber = 0
            return True
        
        # Check the Actor's current casts for Kevin, the lowest value found so far,
        # or queue them for further examination
        queue = []
        
        for movie, cast in self.casts.items():
            if self in cast:
                for actor in cast:
                    # Kevin Bacon directly appears in one of the actor's movies
                    if actor.name == BACON:
                        self.baconNumber = 1
                        self.baconPath = [(BACON, movie)]
                        return True
                    
                    # The actor has not examined their own Bacon Number
                    hold = (actor, movie)
                    queue.append(hold)
        
        while len(queue) > 0:
            path = queue[0]
            
            if len(path) > 0:
                actor = path[0]
                movie = path[1]

                for film, cast in actor.casts.items():
                    for member in cast:
                        if member.name == BACON:
                            actor.baconNumber = 1
                            actor.baconPath = [(BACON, film)]
                            self.baconNumber = actor.baconNumber + 1
                            self.baconPath = actor.baconPath[:] + [(actor.name, movie)]
                            return True
                        else:
                            if member.name != self.name and self.casts.get(movie, None) == None:
                                queue.append((member, film))
            
            queue.pop(0)
            
        # If, after searching all actors, no paths were found, indicate this
        self.baconPath = []
        self.touchPath = []
        self.baconNumber = -1
        return False


def main():
    movies = ['Apollo13', 'Armageddon', 'DieHard', 'Footloose', 'TheRock', 'TheRoom']
    actors = {}
    cast = []
    crew = []
    
    # Read in the cast lists and create actor nodes
    for movie in movies:
        del cast[:]
        cast = []
        
        with open(movie + ".txt", 'r') as file:
            cast = file.read().split('\n')
        
        del crew[:]
        crew = []
        
        for actor in cast:
            name = actors.get(actor, None)
            
            if name == None:
                name = Actor(actor)
    
            crew.append(name)
        
        for actor in crew:
            actor.addMovie(str(movie), crew[:])
            actors[actor.name] = actor
    
    # Testing some actors
    # Kevin Bacon
    Baconator = actors.get(BACON)
    Baconator.findBacon()
    Baconator.printBaconPath()
    
    # 1 degree
    JohnLithgow = actors.get("John Lithgow")
    JohnLithgow.findBacon()
    JohnLithgow.printBaconPath()
    
    # 2 degree
    NicolasCage = actors.get("Nicolas Cage")
    NicolasCage.findBacon()
    NicolasCage.printBaconPath()
    
    BruceWillis = actors.get("Bruce Willis")
    BruceWillis.findBacon()
    BruceWillis.printBaconPath()

    TonyTodd = actors.get("Tony Todd")
    TonyTodd.findBacon()
    TonyTodd.printBaconPath()
    
    # No Links (listed)
    TommyWiseau = actors.get("Tommy Wiseau")
    TommyWiseau.findBacon()
    TommyWiseau.printBaconPath()
    
main()
