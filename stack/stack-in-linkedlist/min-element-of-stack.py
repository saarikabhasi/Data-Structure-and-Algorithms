"""
cracking coding interview page 98

Design a stack which does push,pop  and has a function min which returns min element? 
Push,pop,min should all operate in O(1) time

Can be implement with list or stack 
Approach 1: have an additional array/stack, which stores minimum value at each step. 
            space is O(n) for all the cases
Approach 2: have an additional array/stack, which compares and stores minimum value at each step.
            space is O(n) for worst case scenerios

Implementing approach 2, implementing with additional stack

I have implmented with two stacks. 
One is mainStack- which is the actual stack where contents are pushed
second is minStack- stores min element 

Push:
For every push, I check if min stack top is less that new element. 
Push new element only if new element is less that existing top min element.

Pop: 
Remove given element from min stack only if min stack top is equal to the element to be removed from main Stack.



"""
import stack
class Minstack():
    def __init__(self):
        self.minStack = stack.Stack()
        self.mainStack = stack.Stack()

    def push(self,data):
        self.mainStack.push(data)
        if self.minStack.top == None:
            #min stack is empty
            self.minStack.push(data)
        elif self.minStack.top.data > data:
            self.minStack.push(data)
        return
    def peek_minStack(self):
        if self.minStack.top !=None:
            return self.minStack.top.data
        else:
            return None
    def peek_mainStack(self):
        return self.mainStack.peek()
    
    def isminstackEmpty(self):
        return self.minStack.top == None
    
    def pop(self):
        data = self.mainStack.peek()
        if self.peek_minStack() != None and self.peek_minStack() == data:
            #remove from min stack
            self.minStack.top = self.minStack.top.next
        self.mainStack.pop()


    def print_minStack(self):
        
        if not self.isminstackEmpty():
            print("printing contents of min Stack")
            p = self.minStack.top
            while p!=None:
                print(p.data)
                p = p.next
        else:
            print("Min stack is empty")
        return

    def print_mainStack(self):
        
        if not  self.mainStack.isempty():
            print("printing contents of main Stack")
            p = self.mainStack.top
            while p!=None:
                print(p.data)
                p = p.next
        else:
             print("Main stack is empty")
        return
    
    def getMin(self):
        if self.minStack.top:
            print("Minimum element is "+str(self.minStack.top.data)) 
        else:
            print("Minimum element is "+str(self.minStack.top)) 
        return

    


obj = Minstack()
obj.push(5)
obj.push(6)
obj.push(3)
obj.push(7)
obj.getMin()
obj.print_minStack()
obj.print_mainStack()
obj.pop()
obj.pop()
obj.getMin()
