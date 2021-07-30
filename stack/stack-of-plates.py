"""
cracking coding interview page #99




"""
import stack

class newStack():
    def __init__(self) -> None:
        self.top = None
        self.stack = []

class SetofStacks():
    def __init__(self) -> None:
        self.top = None
        self.stack = []
        self.maxthreshold = 3
        self.size = 0
        self.next = None
        

    def isstackempty(self):
        return self.top == None

    def push(self,data):
        if self.isstackempty():
            #first push
            self.stack.append(data)
            self.top = data
            self.size +=1
        else:
            #data present already
            if self.size >=self.maxthreshold:
                # if self.size % self.maxthreshold >1:
                    #more than 1 stack is required
                if (self.size -self.maxthreshold)%self.maxthreshold == 0:
                    #new stack is yet to be created
                    
                    #create new stack
                    obj= self.SetofStacks()
                    obj.stack.append(data)
                    self.top = data
                    self.size +=1
                    self.next = obj.stack[0]
        
            else:

                #main stack
                self.stack.append(data)
                self.top = data
                self.size +=1

       

        
    pass

obj = SetofStacks()



