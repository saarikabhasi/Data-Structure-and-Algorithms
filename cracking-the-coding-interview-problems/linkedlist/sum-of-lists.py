"""
Cracking the coding interview 
page #95, question #2.5

You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the 1's digit is at the head of the list. 
Write a function that  adds the two numbers and returns the sum as a linked list.

Example:
7->1->6 + 5->9->2  That is 617+295 = 912
head of list 1 is 7
head of list 2 is 5

Follow up 

Suppose the digits are stored in forward order. Repeat the above problem. 
6->1->7 + 2->9->5  That is 617+295 = 912

head of list 1 is 6
head of list 2 is 2

"""
class Stack():
    def __init__(self) -> None:
        self.s = [None]*6
        self.top = None

    def push(self,data):
        if self.top == None :
            self.top = 0
            self.s[self.top] = data
        else:
            self.top +=1
            self.s[self.top ] =data

    def pop(self):
        if self.top == -1:
            print("stack empty")
            self.top = None
        else:
            t = self.s[self.top]
            # self.s.pop(self.top)
            del self.s[self.top]
            self.top -=1
        return t
    def show(self):
        p = self.top
        while p !=None:
            print(self.s[p])
            p -=1
        print("============")
        

class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class singlelinkedlist():
    def __init__(self) -> None:
        self.head = None
    
    def insert(self,data):
        """
        insert the data to the linked list
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            p=self.head
            while p.next:
                p = p.next
            p.next =node
        
    def show(self):
        print("------------------------")
        p =self.head
        if p:
            while p:
                print(p.data)
                p = p.next

        else:
            print("List empty")
        print("------------------------")

class addDigits():
    def __init__(self,lobj1,lobj2) -> None:
        # self.result = super().__init__()
        self.d1 = lobj1
        self.d2 = lobj2
        

    def addDigitsinreverse(self):
        """
        Add the digits stored in reverse order, Meaning head points to unit digit
        return other list if any of the list is empty

        """

        if self.d1.head == None:
            return self.d2
        elif self.d2.head == None:
            return self.d1
        else:
            p1 =self.d1.head
            p2 =self.d2.head
            carry =0 
            self.result = singlelinkedlist()
            while p1 !=None or p2!=None:
                if p1 and p2:
                    r = p1.data + p2.data +carry
                    p1 = p1.next
                    p2 = p2.next
                elif p1:
                    r = p1.data+carry
                    p1 = p1.next
                else:
                    r = p2.data+carry
                    p2 = p2.next

                carry = 0
                if r>=10:
                    self.result.insert(r%10)
                    carry = r //10
                else:
                    self.result.insert(r)
            
            if carry >0:
                self.result.insert(carry)
                
                
        return self.result
                
    def addDigitsinforward_withstack(self):
        """
        Add the digits stored in list in forward order. Meaning head points to last place of digit
        
        """
        if not self.d1.head:
            return self.d2
        elif not self.d2.head:
            return self.d1
        else:
            
            p1 = self.d1.head
            p2 = self.d2.head
            
            stack = Stack()
            result = singlelinkedlist()
            
            s1 = self.d1.head 
            s2 = self.d2.head

            size1 = 0
            size2 = 0

            while s1:
                size1 +=1
                s1 =s1.next

            while s2:
                size2 +=1
                s2 =s2.next

            if size2>size1:
                pass
            else:
                pass
        

            

            while p1 or p2:
       
                if not p1:
                    stack.push( p2.data)
                    p2 = p2.next
                elif not p2:
                    stack.push( p1.data)
                    p1 = p1.next
                else:
                    stack.push(p1.data + p2.data)
                    p1 = p1.next
                    p2 = p2.next

                
            
            carry = 0 
            while stack.top>=0:
                add = stack.pop()
                
                node = Node(add%10+carry)
                if add >=9:
                    
                    if result.head == None:
                        # 
                        result.head = node
                        
                    
                    else:
                        node.next = result.head
                        result.head = node

                    carry = 1
                        
                        
                else:
                    if result.head == None:

                        result.head = node
                    else:
                        node.next = result.head 
                        result.head = node
                        carry = 0
                
        return result


                    
                
            
            

# lobj1 = singlelinkedlist()
# lobj1.insert(8)
# lobj1.insert(9)
# lobj1.show()

# lobj2 = singlelinkedlist()
# lobj2.insert(2)
# lobj2.insert(0)
# lobj2.insert(1)

# lobj2.show()

# aobj1  = addDigits(lobj1,lobj2)
# res1 = aobj1.addDigitsinreverse()
# print("Result")
# res1.show()

#example2 forward
lobj3 = singlelinkedlist()
# lobj3.insert(6)
lobj3.insert(1)
lobj3.insert(7)

lobj4 = singlelinkedlist()
lobj4.insert(2)
lobj4.insert(9)
lobj4.insert(5)

aobj2  = addDigits(lobj3,lobj4)
res2 = aobj2.addDigitsinforward_withstack()
print("Result")
res2.show()


