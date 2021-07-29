"""

cracking coding interview page #98

Describe how will implement three stack with 1 array

Approach 1: Divide array by 3 (space might be unused)
Approach 2: saving up space

"""
class Stack():
    def __init__(self):
        self.data = None
        self.top = None
        self.next = None
    
    def setData(self,data):
        self.data = data

    def isstackempty(self):
        return self.top == None

    def print(self):
        print("_____")
        p = self
        # print(p)
        # print(p.top)
        # if p.next is not None:
        #     print(p.next)
        # else:
        #     print(p.next)
        while p.next!=None:
            print(p.data)
            p = p.next

class Array():
    def __init__(self,size):
        self.a=[None]*size
        self.free =0
        self.prev_free = -1
        # self.stackobjects =[]
        # # self.stackobjects = [0]*stackobjects
        # for _ in range(1,stackobjects):
        #     self.stackobjects.append(Stack(1))
    
    # def isarrayempty(self,obj):
    #     #array is empty when all stacks are empty
    #     for i in range(len(self.stackobjects)):
    #         if self.stackobjects[i].top != None:
    #             return False
    #     return True


    def push(self,data,obj):

        if self.free !=None:
            #array is not full
            obj.setData(data)
            self.a[self.free] = obj.data
            
            if obj.top is not None:
                # stack has other entries
                print("top object b4",obj.top)
                obj.next = obj.top

            #top pointer pointing to current free index
            # obj.top = obj.data
            obj.top = self.free
            print("top object after",obj.top)
            print("obj next",obj.next)
            #check if there is any empty slot in array
            if self.prev_free == -1:
                self.free +=1
            else:
                self.free =self.prev_free
                self.prev_free = -1

            if self.free >= len(self.a):
                #array is full 
                self.free = None
          
            print(self.free)
        else:
            print("array is full can't push any more items")
            return
    def pop(self,obj):
    
        if self.free == None:
            self.free = len(self.a)-1
        
        
        self.prev_free = self.free
        self.free = obj.top
        self.a[self.free] = None
        obj.top = obj.next
        print(self.free,self.prev_free)
        return
    

    def print(self):
        # print(self.a[0].top.data)
        print("_________")
        c = 0
        for i in self.a:
            
            if i != None:
                print("index[",c,"]",i)

            c +=1





# three stack object
sa = Stack()
sb = Stack()
sc = Stack()

a = Array(4)
a.push(1,sa)
a.push(2,sa)
a.push(3,sa)
a.push(4,sa)
a.pop(sa)


a.print()

a.push(5,sb)
# a.push(3,sc)
a.print()
# a.pop(sa)
# a.print()

# a.push(4,sc)
a.print()
        