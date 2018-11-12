from dllist import *

# A path finder object isolates the logic to perform a path-finding
# problem on:
# 
#   - An underlying `board` object.
# 
#   - A `player` object, which holds the player's current position and
#   other relevant information about the player.
class PathFinder:
    def __init__(self, board, player):
        # The underlying game board on which tiles live
        self.board   = board
        
        # The underlying player object
        self.player  = player

        # The starting coordinates
        self.startX  = player.getX()
        self.startY  = player.getY()
        
        # The width / height of the board
        self.width   = self.board.width
        self.height  = self.board.height

        # A two-dimensional array to store whether or not the tile has
        # been visited.
        self.visited = [[False for x in range(board.width)]
                        for y in range(board.height)]

        # XXX
        self.winning = False

    # Check whether `path` is a valid path
    def checkValidPath(self,path):
        x = path[0][0] #getting the 'x' coordinate of the first element in the path
        y = path[0][1] #getting the 'y' coordinate of the first element in the path
        for t in path[1:]:
            x = x + t[0]                       #recalculate the x coordinate
            y = y + t[1]                       #re-calculate the y coordinate
            
            if (self.canMoveTo(x,y) == False):  #check if the tile is one you can move to..
                return False                    #return False if you can't
        return True

    # Check whether or not there is a wall (or other solid object) at
    # the coordinates (x,y)
    def wallAt(self,x,y):
        return self.board.higherPriorityObjectAt(self.player,x,y)
    
    # Check whether or not we can move to (x,y) I.e., is there a wall
    # there, or is it out of bounds?
    def canMoveTo(self,tx,ty):
        if (tx < 0) or (ty < 0):      #If the x or y coordinates are negative, return False. 
            return False              #You are out of bounds.
        if (self.width <= tx) or (self.height <= ty):  #If they are greater than the width or height of the board
            return False                               #return False
        elif self.wallAt(tx,ty):                       #If there is a wall, return False
            return False
        else:
            return True                                 #return True otherwise.
            
    def canSolve(self, toCoordinate):
       return (self.findPath(toCoordinate) != False)  #If there is a path, then you can solve. 

    def findPath(self, toCoordinate):
        nxt = [(self.startX, self.startY)]  #create a list 'nxt', so we know what tiles to explore next.
        #These represent tile movements (up, down, left and right).
        #I will add these to a tile to make my life easier. 
        le = (-1, 0)
        r = (1,0)
        u = (0,-1)
        d = (0, 1)
        coord0 = (self.startX, self.startY)                              #This represents my starting tile.
        self.visited[coord0[0]][coord0[1]] = [(self.startX, self.startY)] #Here, I am initializing the matrix at our starting coordinate to hold a partial path. 
        
        while nxt:              #while our list is not empty, in other words while we have more to explore...
            
            coord0 = nxt.pop(0) #coord0 will represent the tile we are exploring currently. I get this by popping it off nxt.
            
            #Here, I define coordinates that represent the tiles above, left, right and below the tile we are currently exploring.
            above = (coord0[0], coord0[1]-1)
            down = (coord0[0], coord0[1]+1)
            right = (coord0[0]+1,coord0[1])
            left = (coord0[0]-1,coord0[1])

            if coord0 == toCoordinate:                    #In the event that we reach our tile,
                return self.visited[coord0[0]][coord0[1]] #return the path stored in the matrix. 

            #For this series of if statements, I check if we are able to move above, down, to the right, and to the left.
            #I also check that the tile hasn't been visited by checking that self.visited at that coordinate is equal to False. 
            #If both conditions pass, add that coordinate to our list or next tiles to explore.
            #And set self.visited at that path to be equal to the path previously, plus the move that got us to that path.
            
            if self.canMoveTo(above[0], above[1]) and self.visited[above[0]][above[1]] == False:
                nxt.append((above[0], above[1]))
                self.visited[above[0]][above[1]] =  self.visited[coord0[0]][coord0[1]] + [u]
               
            if self.canMoveTo(down[0], down[1]) and self.visited[down[0]][down[1]] == False:
                nxt.append((down[0], down[1]))
                self.visited[down[0]][down[1]] =  self.visited[coord0[0]][coord0[1]] + [d]
                                                                   
                
            if self.canMoveTo(right[0], right[1]) and self.visited[right[0]][right[1]] == False:
                nxt.append((right[0], right[1]))
                self.visited[right[0]][right[1]] =  self.visited[coord0[0]][coord0[1]] + [r]

                 
            if self.canMoveTo(left[0], left[1]) and self.visited[left[0]][left[1]] == False:
                nxt.append((left[0],  left[1]))
                self.visited[left[0]][left[1]] =  self.visited[coord0[0]][coord0[1]] + [le]

        return False    #if we run out of moves before reaching the tile, return False.
                    
