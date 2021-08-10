"""
Implementing circular queue in Array
Difference between circular(CQ) and simple queue(SQ) is that,
In SQ, After the elements are removed, the removed position is not used until all the entries are removed in a set.
In CQ, if rear reaches the end of array, for next enQ it checks if the next poistion (ie 0)is available. 
So basically in CQ, elements are removed and added in circular fashion

Example:

SQ Array
*******

Enq A
Enq B
Enq C
display SQ
C 
B 
A 
--------
Deq A
Deq B
display SQ
C 
None 
None 
--------
Enqueue failed as Queue is full  (enQ failed even though there is a space available in array)
--------
Enqueue failed as Queue is full (enQ failed even though there is a space available in array)
--------
display SQ
C 
None 
None 
--------


CQ Array
*******

EnQ A 
--------
EnQ B 
--------
EnQ C 
--------
Displaying CQ
A
B
C
------------
peek is A 
--------
DeQ A 
--------
DeQ B 
--------
Displaying CQ
C
------------
peek is C 
--------
EnQ D (Enq sucess)
--------
EnQ E 
--------
peek is C 
--------
Displaying CQ
C
D
E
------------




"""

class circularQueue:
    def __init__(self,maxsize) -> None:
        """
        initializing Q object
        """
        self.front = -1
        self.rear = -1
        self.size = maxsize
        self.q = [None]*self.size
    
    def isEmpty(self):
        """
        returns true if Q is empty

        """
        return self.front==self.rear == -1
    
    def isFull(self):
        """
        return true if Q is Full
 
        """
 
        return (self.rear +1) % self.size == self.front
        
    def peek(self):
        return self.q[self.front]
    def enqueue(self,data):
        """
        Add data to the Queue
        """
        if not self.isFull():
            if self.rear == self.front == -1:
                #first entry
                self.rear = self.front = 0
    
            else:
                #other entry exist
                self.rear =( self.rear + 1 ) %self.size
            
            self.q[self.rear] =data
            print("EnQ",self.q[self.rear],"\n--------")
        else:
            print(" EnQ fail, Q is Full")
        return
    def dequeue(self):
        """
        Remove data from array
        
        """
        if not self.isEmpty():
            #Q is not empty
            print("DeQ", self.q[self.front],"\n--------")
            self.q[self.front]=None

            if self.rear == self.front:
                #one element
                self.rear = -1
                self.front = -1
            else:
                self.front = (self.front+1)%self.size
            
        else:
            print("DeQ fail, Q is Empty")
        return

    def print(self):
        """
        display queue 
        
        """
        print("Displaying CQ")
        if self.isEmpty():
            print("Q is empty")
        elif self.rear >=self.front:
            #print from front to rear
            for i in range(self.front,self.rear+1):
                print(self.q[i])
        else:
            #rear<front

            # display from front to end of array
            for i in range(self.front,self.size):
                print(self.q[i])
            # display from 0 till rear 
            for i in range(0,self.rear+1):
                print(self.q[i])

        print("------------")
obj = circularQueue(3)
obj.enqueue("A")
obj.enqueue("B")
obj.enqueue("C")
obj.print()
print("peek is",obj.peek(),"\n--------")
obj.dequeue()
obj.dequeue()
obj.print()
print("peek is",obj.peek(),"\n--------")
obj.enqueue("D")
obj.enqueue("E")
print("peek is",obj.peek(),"\n--------")
obj.print()

            
                