# Doubly-linked list implementation

# 
# Modify this file
#

class NoSuchLink(Exception):
    pass

# A double link has three fields
#  - data <-- The underlying data the link is storing
#  - back <-- A reference to the previous element
#             (possibly None)
#  - next <-- A reference to the next element
#             (possibly None)
class DoubleLink:
    def __init__(self,data,back,nxt):
        self.data    = data
        self.prevLnk = back
        self.nextLnk = nxt

    # Make this object work with "deep" equality. See this
    # StackOverflow post:
    #     https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes-in-python
    def __eq__(self, other): 
        if (other):
            return self.__dict__ == other.__dict__
        #dict is a python hash, stores keys and values. 
        return False

    def hasNext(self):
        return (self.nextLnk != None)
    
    def hasPrev(self):
        return (self.prevLnk != None)

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextLnk

    def getPrev(self):
        return self.prevLnk

    def setNext(self, n):
        self.nextLnk = n

    def setPrev(self, n):
        self.prevLnk = n

# A doubly-linked list
# 15 points
class DLList:
    # Constructor for empty doubly-linked list
    def __init__(self):
        self.first = None        

    # Calculate the size of the list
    #  1 point
    def size(self):
        count = 0 
        link = self.first         #assign self.first to a variable 
                                  #doesn't affect self.first.
        
        while (link != None):     #while the link is 'None'...
            link = link.getNext() #redefine link to self.get
            count = count + 1     #increment count 
        return count              #return count, which is the number of times we went through the link
                
    # Check whether this doubly-linked list is equal to another
    # list. Two lists should be equal when they contain exactly the
    # same sequence of elements, where the comparison of each object
    # happens using the == operator.
    # 
    # I.e., two lists (e.g., created using distinct calls to the
    # DoublyLinkedList constructor and subsequent calls to add)
    # containing the sequence of elements: 
    # 
    #   (1,1), (0,1), (1,0)
    # 
    # Should be equal
    #   2 points
    def __eq__(self, other):
        node = self.first          #assign self.first to a variable 
        other_node = other.first   #assign other.first to a variable 
        while (node!= None) & (other_node != None): #compare the variables in node and other
            if node.data != other_node.data:        #if the data is not the same, the lists are not equivalent 
                return False
            node = node.getNext()                   #reset node so it is the next link
            other_node = other_node.getNext()       #reset other_node so it is the next link
        return True

    # Add some data at the head of a doubly-linked list. This should
    # take O(1) time
    #   2 points
    def add(self, data):
        data_object = DoubleLink(data,None,None)     #create a DoubleLink (DL) object containing the data
        if (self.first == None):                     #if link is empty,
            self.first = data_object                 #replace the first link with the DL object
        else:                                        #otherwise, if there is more than one link...
            self.first.setPrev(data_object)          #set the previous link in self.first to the DL object with the current data, None as the previous, and reverse as the previous. 
            data_object.setNext(self.first)          #set the next link in self.first to the DL object                
            self.first = data_object                 #set the first link as the data
        
    # Remove some piece of data from the list. Compare for equality of
    # data using ==
    #   2 points
    def remove(self,data):
        node = self.first   #reassign self.first to a variable, so the variable
                            #can be altered later without altering self.first. 
        if (node.data == data) & (node.getNext() == None):
            node = None

        if node.data == data:
            self.first.getNext().setPrev(None)
            self.first = node.getNext()
        else:           
            while(node != None):
                if node.data == data:
                    self.first.getPrev().setNext(self.first.getNext())
                    self.first.getNext().setPrev(self.first.getPrev())
                else:
                    node = node.getNext() #maybe self.first?

    # Check whether the list contains `data`
    #   2 points
    def contains(self, data):
        node = self.first

        if (node == None):
            return False
        if node.data == data:
            return True
        else:
            while (node != None):
                if node.data == data:
                    return True
                node = node.getNext()
        return False

    # Reverse this linked-list in place. After a call to reverse, the
    # last element of the list should become the first, etc...
    #   2 points
    def reverse(self):
        reverse = None          #initialize a variable reverse as  None
        current = self.first    #and "current' as self.first

        while (current != None):                                #while current has a next link..
            reverse = DoubleLink(current.data, None, reverse)   #redine reverse by creating a DoubleLink object.
            current =  current.getNext()                        #reinitialize current as the next link                               
        self.first = reverse                                    #self.first should now equal reverse.

    # Convert the elements of this list to an array
    #  2 points
    def toArray(self):
        newArray = []          #create an empty list to store the array in
        node = self.first
        
        while (node != None):
            newArray.append(node.data) #append the data in the node to the list
            node = node.getNext()      #reassign node as getNext to access next node
            
        return newArray                #return the array
    
    # Get the `i`th element of the list
    # Precondition: i < self.size()
    # Otherwise, raise NoSuchElementException
    #  2 points
    def getIth(self, i):
        counter = 0
        node = self.first

        #This function works by counting up to the i'th element, setting node = node.getNext()
        # if it doesn't find the element and then returning node.data at that element when it finds it. 

        if i > self.size() or (self.first == None):
            raise NoSuchElementException
        else:
            while (counter != i):
                node = node.getNext()
                counter = counter + 1
        return node.data
