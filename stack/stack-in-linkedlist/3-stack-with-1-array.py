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
        while p.next!=None:
            print(p.data)
            p = p.next

class Array():
    def __init__(self,size):
        self.a=[None]*size
        self.free =0
        self.prev_free = -1



    def push(self,data,obj):
   
        if self.free !=None:
            #array is not full
            obj.setData(data)
            self.a[self.free] = obj.data
            
            if obj.top is not None:
                # stack has other entries
                obj.next = obj.top

            #top pointer pointing to current free index

            obj.top = self.free

            #check if there is any empty slot in array

            if self.prev_free == -1:
                self.free +=1
            elif self.prev_free == None:
                self.free = None
            else:
                self.free =self.prev_free
                self.prev_free = -1

            if self.free is not None and self.free >= len(self.a):
                #array is full 
                self.free = None
          

        else:
            print("array is full can't push any more items")
            return
    def pop(self,obj):
        print("pop")

        self.prev_free = self.free
        self.free = obj.top
        self.a[self.free] = None
        obj.top = obj.next
        
        return
    

    def print(self):
        print("_________")
        c = 0
        for i in self.a:

            print("index[",c,"]",i)

            c +=1
        print("_________")




# three stack object
sa = Stack()
sb = Stack()
sc = Stack()

a = Array(4)

# a.push("a",sa)
# a.push("b",sa)
# a.push("c",sa)
# # a.push(4,sa)
# a.print()
# a.pop(sa)
# a.print()
# a.pop(sa)
# a.print()
# a.pop(sa)
# a.print()
# a.pop(sa)
# a.print()



a.push("a",sa)
a.push("b",sb)
a.push("c",sc)
a.push("d",sa)
a.print()
print("pop in sc")
a.pop(sc)

a.print()
a.push("e",sc)
a.print()
# print("push 6 in sb")
a.push("f",sb)
# print("pop in sa")
a.pop(sa)
a.print()
# print("pop in sa")
a.pop(sa)
a.print()
# print("push 7 in sb")
a.push(7,sb)
a.print()
# print("push 8 in sb")
# a.push(8,sb)
# a.print()
# print("push 9 in sc")
# a.push(9,sc)
# a.pop(sc)
# a.print()
# print("pop in sa")
# a.pop(sa)
# a.print()







        