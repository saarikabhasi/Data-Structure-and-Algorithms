"""
example: 3->2->1

top pointer points to top most element in stack. Initial top value is -1. 
Operation: 
Push: insert an element
    push(4): 4->3->2->1
Pop: remove an element from stack
    pop(): returns 4 

isempty: checks if the stack is empty
    return True if empty else False

    
peek : returns top most element

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top= None

    def isempty(self):
        if self.top == None:
            return True
        return False

    def peek(self):
        if self.isempty():
            return -1
        return self.top.data
         
    
    def push(self,data):
        new_node = Node(data)
        if self.top == None:
            #list empty
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        return 
        

    def pop(self):
        if not self.isempty():
            self.top =self.top.next 
        return

    def print(self):
        p = self.top
        while p!=None:
            print(p.data)
            p = p.next
        print("-------")

# obj = Stack()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.print()
# print("stack is empty?",obj.isempty())
# print("stack top most element",obj.peek())
# obj.pop()
# obj.print()
# obj.pop()
# obj.print()

        


   

