"""
Implementing circular Q in Linked list 

"""
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class cQueue:
    def __init__(self,maxSize) -> None:
        self.front = None
        self.rear = None
        self.maxsize = maxSize
        self.size =0

    def isFull(self):
        return self.size == self.maxsize
    
    def isEmpty(self):
        return self.front ==self.rear==None
    
    def peek(self):
        return self.front.data

    def print(self):
        p = self.rear
        if p == self.front:
            #single item
            print(p.data)
        else:
            while p.next != self.rear:
                print(p.data)
                p = p.next
            print(p.data)

    def enqueue(self,data):
        if self.isFull():
            print("EnQ Fail, Full")
        else:
            newNode = Node(data)
            print("EnQ",data)
            if self.front == None:
                #first enQ
                self.front = self.rear = newNode
                # self.front.next = self.rear
                
               
            else:
                newNode.next = self.rear
                self.rear = newNode

            self.front.next = newNode
            self.size +=1
            
        return
    
    def dequeue(self):
        if self.isEmpty():
            print("DeQ fail, Empty")
        else:
            print("DeQ",self.front.data)
            if self.front == self.rear:
                #one item
                self.front.data=None
                self.front = None
                self.rear = None
            else:
                p =self.rear
                while p.next != self.front:
                    p = p.next
                self.front.data = None
                self.front = p
                p.next =self.rear
            self.size -=1

        return

        

            
c = cQueue(3)
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.enqueue(4)
c.print()
c.dequeue()
c.print()
c.enqueue(5)
c.print()
print("peek",c.peek())