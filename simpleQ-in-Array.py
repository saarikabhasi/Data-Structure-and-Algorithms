"""
Implementing Simple Queue using array 

front -  to remove item 
rear - to add item

initally front and rear is -1

* Empty Queue : Queue is empty if both front and rear is equal

* Full Queue : Queue is full if rear has reached its size




"""
class simpleQueue:
    def __init__(self,size) -> None:
        self.front = -1 
        self.rear = -1
        self.size = size 
        self.queue = [None]* self.size # create array of given size
    
    def isEmpty(self):
        """
        checks if Q is empty. 
        return True if empty.

        """
        return self.front == self.rear == -1

    def isFull(self):
        """
        checks if Q is full. 
        return True if full.
        
        """
        return self.rear == self.size -1

    def enqueue(self,item):
        """
        Adds an item to the queue
        item is added to the rear end
        """
        if self.isEmpty():
            #first item in Q
            self.front +=1
        else:
            if self.isFull():
               print('Enqueue failed as Queue is full','\n--------') 
               return 
            
        self.rear += 1
        
        self.queue[self.rear] = item
        print("Enq",self.queue[self.rear])

            
        
                
        return
    def dequeue(self):
        """
        Removes an item to the queue
        item removed from front 

        """
        if not self.isEmpty():
            print("Deq",self.queue[self.front])
            self.queue[self.front] = None
            if self.rear == self.front:
                #last item in list
                self.front = -1
                self.rear = -1
            else:
                self.front +=1
            
        else:
            print('Dequeue failed, as Q is Empty')
            return
        

    def print(self):

        """
        print queue
        """
        print("display SQ")
        p = self.rear
        if self.isEmpty():
            print('Print failed, as Q is empty') 
            return

        while p != -1:
            print(self.queue[p],'\t')
            p -=1
        print("--------") 

qobj = simpleQueue(3)

qobj.enqueue("A")
qobj.enqueue("B")
qobj.enqueue("C")
qobj.print()
qobj.dequeue()
qobj.dequeue()
qobj.print()
qobj.enqueue("D")
qobj.enqueue("E")
qobj.print()

