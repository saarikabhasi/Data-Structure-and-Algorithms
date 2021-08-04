"""
cracking coding interview page #99s

Design a stack of plates. 
Set of stacks is composed of many stacks and should create a new stack once the previous once exceeds the capacity
push(),pop() should behave identically to a single stack. 



"""


class Setofstacks():
    def __init__(self) -> None:
        self.stacks=[]
        self.top = None
        self.threshold = 2
        self.freeslot = None
    def isempty(self):
        return self.top == None
    def createStacks(self,data):
        l = list()
        l.append(data)
        self.stacks.append(l)
        self.top = self.stacks[-1][-1]
        return
    def push(self,data):
        if self.top == None or len(self.stacks[-1])>=self.threshold:
            #stack is empty
            self.createStacks(data)
        else: 
            #in middle of stack
            # if there is a free slot, push item in there
            if self.freeslot != None:
                self.stacks[self.freeslot].append(data)
                self.freeslot = None
            else:
                self.stacks[-1].append(data)
                self.top = self.stacks[-1][-1]
        return
    
    def pop(self):
        if not self.isempty():
            if len(self.stacks[-1]) <=1:
                #last list has 1 or empty list ex:[[1,2],[3]] or [[1,2],[]]
                #so delete entire list
                self.stacks.pop()

                if len(self.stacks) == 0:
                    self.top = None
                else:
                    self.top = self.stacks[-1][-1]

            else:
                #last list has  more than 1 element. ex:[[1,2][3,4]]
                self.stacks[-1].pop() # ex:[[1,2][3]]
                self.top = self.stacks[-1][-1]
        else:
            print("stack is empty")
        return

    def peek(self):
        return self.top
    def print(self):
        print(self.stacks)
    def popAt(self,index):
        """
        index is the stack number

        delete element in given index. 
        ex: [[1,2],[3,4]] 
        popat(0)-> [[2],[3,4]] (return the top value of given stack number and removes it. Also returns -1 if the stack is empty)
        push(5) ->[5,2][3,4]]
        popat(0) ->[[2][3,4]]

        """
        if not self.isempty():
            stacktobeemptied = self.stacks[index]
            if len(stacktobeemptied) == 0:
                return -1
            elif len(stacktobeemptied) == 1:
                return stacktobeemptied.pop()
            else:
                stacktobeemptied.pop()
                #self.top = stacktobeemptied[-1]
                
            self.freeslot = index


        else:
            print("stack empty")
        return
        

        
obj = Setofstacks()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.print()
obj.popAt(0)
obj.print()
obj.push(20)
obj.print()
obj.push(21)
obj.print()
obj.popAt(0)
obj.print()
obj.popAt(2)
obj.print()
obj.pop
obj.print()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.print()
# print("top element is ",obj.peek())
# obj.pop()
# obj.print()
# print("top element is ",obj.peek())

# obj.push(5)
# obj.push(6)
# obj.push(7)
# obj.push(8)
# obj.print()
# print("top element is ",obj.peek())

# obj.pop()
# obj.print()
# print("top element is ",obj.peek())
# obj.pop()
# obj.print()
# print("top element is ",obj.peek())
# obj.pop()
# obj.print()
# print("top element is ",obj.peek())
# obj.pop()
# obj.pop()
# obj.pop()
# obj.print()
# print("top element is ",obj.peek())
# obj.pop()
# obj.print()
# print("top element is ",obj.peek())



    






