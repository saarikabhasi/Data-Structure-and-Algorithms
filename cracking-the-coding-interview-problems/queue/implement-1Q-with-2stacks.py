"""
Cracking the coding interview page # , problem #

Implement a queue with two stacks
stack1  is main stack
stack2 is  secondary stack

* all the enqueue(s) happen in stack1
* In dequeue, check if stack2 is empty.
if stack2 is empty:
    pop and push items from stack1 to stack2
    pop the last push item from stack2
if stack2 is not empty:
    the pop item from stack2



"""
class stack:
    def __init__(self,size) -> None:
        self.top = -1
        self.s = [None]*size

    def peek(self):
        return self.top

    def isFull(self):
        return self.top == len(self.s)-1
    def isEmpty(self):
        return self.top == -1
    def push(self,data):
        
        if self.isEmpty():
            # print("empty")
            self.top = 0
        elif self.isFull():
            # print("full")
            return 
        else:
            self.top +=1

        self.s[self.top] = data
        # print(self.s)
        return
    def pop(self):
        # print("pop of",self.s[self.top])
        if not self.isEmpty():
            self.s[self.top] =None
            self.top -=1

        return 
    def print(self):
        p = self.top
        for i in range(0,p):
            print(self.s[i])

class twostackQ():
    def __init__(self,size) -> None:
        self.stack1 = stack(size)
        self.stack2 = stack(size)


    def enqueue(self,data):
       
        self.stack1.push(data)
        return
    def dequeue(self):
        print("Dq")
        if self.stack2.top >-1:
            print("remove from stack2")
            t = self.stack2.peek()
            self.stack2.pop()
        else:
            print("push from stack1 to stack2")
            p =self.stack1.top
            for i in range(p,-1,-1):
                self.stack2.push(self.stack1.s[i])
                self.stack1.pop()
            t =self.stack2.peek()
            self.stack2.pop()
    
            
        return t
             
    def print(self,sn):
        if sn ==1:
            print("stack1")
            p =self.stack1.top
            if p==-1:
                print("stack1 empty")
            # print(p)
            for i in range(p,-1,-1):
                print(self.stack1.s[i])
        if sn == 2:
            print(" stack2")
            p =self.stack2.top
            if p==-1:
                print("empty")
            # print(p)
            for i in range(p,-1,-1):
                print(self.stack2.s[i])
        print("----------------------------")
        return

q = twostackQ(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print(1)
q.dequeue()
q.print(2)
q.dequeue()
q.enqueue(4)
q.print(2)
q.print(1)
q.dequeue()
q.print(2)
q.print(1)


