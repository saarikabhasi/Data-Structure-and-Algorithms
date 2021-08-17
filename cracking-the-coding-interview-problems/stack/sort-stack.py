"""
cracking the coding interview page #99 problem #3.5

Sort a stack such that the smallest items are on the top. You can use additional Temporary stack,
but may not copy the elements into any other Data structures(sucha as array). 
The stack supports: push,popm peek, isEmpty

1. 2 stacks -mainstack and tempstack
2. Push
    if the new data is greater than given mainstack top:
        pop elements from mainstack & push to tempstack till data < mainstack top
        push new data to mainstack
        pop  from tempstack & push elements back to mainstack
    else:
        push new data to mainstack
3. pop the topmost element from mainstack

Time complexity:
Push:
    worst case:
        pop from mainstack :O(n)
        push to main stack: O(n)
        pop & push :O(n)
        overall:O(n)
    best case:
        O(1)
POP:
    worst & best case: o(1)
    



"""
class stack():
    def __init__(self) -> None:
        self.top = -1
        self.size  = 7
        self.stack = [None]*self.size  #lets assume stack doesn't have size limit
    def isEmpty(self):
        return self.top == -1
    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        return None
    def isFull(self):
        return self.top == self.size -1
    def push(self,data):
        if self.top == -1:
            self.top = 0
        else:
            self.top +=1
            if self.isFull():
                print("full",self.top)  
                return 
               
        # print(self.top)  
        # self.stack[self.top]=data
        self.stack[self.top] =data
        # print("pushed ",data," to stack")
        return
    
    def pop(self):
        if not self.isEmpty():
            t = self.stack[self.top]
            self.stack[self.top] = None
            self.top -=1
            # print("Popped",t, "from stack")
            return t
        else:
            print("Pop fail, stack full")
            return 
    def print(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
class sortStack():
    def __init__(self) -> None:
        self.mainstack = stack()
        self.tempstack = stack()
        
    def isEmpty(self):
        return self.mainstack.isEmpty()
    def push(self,data):
        
        if self.mainstack.peek() != None and self.mainstack.peek()<data:
                #pop and push data to tempstack until peek is greater than data
                while self.mainstack.peek() != None and self.mainstack.peek()<data:
                    t= self.mainstack.pop()
                    self.tempstack.push(t)

                #add new data to mainstack
                
                self.mainstack.push(data)


                #push back main stack content back
                while self.tempstack.peek() !=None:
                    t = self.tempstack.pop()
                    self.mainstack.push(t)
                   
                    
                

        else:
            #mainstack is empty
            self.mainstack.push(data)
        print("pushed ",data," to main stack")
        return

    def pop(self):
        t = self.mainstack.pop()
        print("removed ", t, "from mainstack")
   


    def print(self):
        self.mainstack.print()

sortstack = sortStack()

sortstack.push(34)
sortstack.push(3)
sortstack.push(31)
sortstack.push(98)
sortstack.push(92)
sortstack.push(23)
sortstack.print()
sortstack.pop()
sortstack.print()
