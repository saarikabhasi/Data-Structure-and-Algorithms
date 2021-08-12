"""
Implementing queue in linked list 

self.front points to node which is next in line to be removed
self.rear points to most recently entered node
self.size counts queue entries
self.maxSize is the maximum possible entries in queue


"""

class Node:
    def __init__(self,item) -> None:
        self.item = item
        self.next = None
        
class Queue:
    def __init__(self,maxSize) -> None:
        self.front = None
        self.rear = None
        self.size = 0
        self.maxSize = maxSize

    def isEmpty(self):
        return self.front == self.rear == None
    def isFull(self):
        return self.size == self.maxSize

    def enqueue(self,data):
        newNode = Node(data)
        if not self.isFull():
            #Q is not Full yet
            if self.isEmpty():
                # First entry 
                self.front  = newNode
            else:
                # other entry exist
                lastNode = self.front
                while lastNode.next:
                    lastNode = lastNode.next

                lastNode.next = newNode
                

            self.rear = newNode
            self.size+=1
        else:
            print('Enqueue failed as Queue is full') 
        return        
    
    def dequeue(self):
        if not self.isEmpty():
            #last node
  
            self.front = self.front.next
            self.size -=1
            if self.front == None and self.size == 0:
                #removed last node, list empty
                self.rear = None 
        else:
            print("Dequeue fail, Queue is empty")
        return  

    def print(self):
        size = self.size
        p = self.front
        flag = True
        while size>=0 and p:
            if flag:
                print("to be removed is:",p.item)
                flag=False
            else:
                print(p.item)    
            p = p.next
        print("__________")
        return
        

        

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.print()