"""
A->B->C->D--
^           |
|           |
|___________| 

Head pointer = A

Insert:
1. Prepend (inset at beginning)
2. Append (inset at end)

Delete:
1. Remove(remove given element)
Assumptions: No duplicate elements

Split a circular list into two:
i/p: A->B->C->D
o/p: A->B->points back to A and C->D-> points back to C

Josephus problem: 

A->B->C->D->points back to A
There four people A,B,C and D standing in a circle.
Like child's game, let's say we want to eliminate some people at every step until we find a winner.
Suppose k is the step size and we have to eliminate kth number, At every step k-1 number of people is skipped.

For example:
k = 2; k-1= 1 (1 person is skipped for every 2 person)
Suppose start pointer is at A. 
Turn 1: A->B->C->D -> points back to A

Step 1: Skip A
Step 2: eliminate B 
Step 3: Skip C
Step 4: eliminate D

Turn 2: A->C->points back to A
Step 1: Skip A
Step 2: eliminate C

Final: A->points back to A
Winner is A.





"""
class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self,data):
        #print("prepend",data)
        new_node = Node(data)
        new_node.next = self.head

        if self.head is None:
            self.head = new_node
            
        else:
            #traverse to find last node
            cur  = self.head
            while cur:
                cur = cur.next
                if cur.next == self.head:
                    break

            cur.next = new_node
            self.head = new_node

    def append(self,data):
        #print("append",data)
        new_node  = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return 
        else:
            new_node.next = self.head
        #traverse to find last node

        cur = self.head
        while cur:
            cur = cur.next
            if cur.next == self.head:
                break
        cur.next = new_node

    def print_list(self):
        cur = self.head
        # print(self.head.data)
        if self.head is None:
            print("List empty")

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                print("____________________")
                break
        return
        

    def remove(self,data):
        #find data
        print("remove",data)
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev == None:
                    # Head node is data
                    if cur.next == self.head:
                        # only one element exist in list
                        self.head = None
                    else:
                        # make head point to next node
                        last_node = self.head

                        while last_node.next != self.head:
                            last_node = last_node.next

                        self.head = cur.next
                        last_node.next = self.head
                    cur = None

                    return
                else:
                    # data exist somewhere after head Node
                    # data may or may not be the last node 

                    if cur.next == self.head:
                        # data is last node
                        prev.next = self.head
                    else:
                        # data is not the last node
                        prev.next = cur.next
                    cur = None
                    return


            else:
                if cur.next == self.head :
                    #reached end
                    print("Unable to find the value",data)
                    break
            prev = cur
            cur = cur.next

    def split_list(self):
        # find length:
        length = 0
        if self.head != None:
            cur = self.head
            # find total length of list
            while cur:
                length+=1
                if cur.next == self.head:
                    if length == 1:
                        print("Can not split list, as only one element exist")
                        return
                    break
                
                cur = cur.next
            #find mid point
            mid = (length)//2
            
            cur = self.head
            i = mid -1
            #split first half 
            while cur:
                if i == 0:
                    nxt = cur.next
                    cur.next = self.head
                    break
                i = i-1
                cur = cur.next
        
        
            #second half
            split_obj = CircularLinkedList()
            new_head = nxt
            while nxt:
                split_obj.append(nxt.data)

                if nxt.next == self.head:
                    nxt.next = new_head
                    break
                nxt = nxt.next
            self.print_list()
            print("\n")
            split_obj.print_list()
    def __len__(self):
        cur = self.head
        length = 0
        while cur:
            length+=1
            if cur.next == self.head:
                break
            
            cur = cur.next
        return length

    def remove_node(self,curNode):
        #print(prevNode==self.head,"prev",prevNode.data, "cur",curNode.data,"head",self.head.data)
        

        if curNode == self.head:

        #if prevNode ==self.head  :
            # remove head node
            #find last node and make last node point to second node
            cur = self.head
            
            while cur.next!=self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            cur.next = self.head.next
            self.head = self.head.next
            prevNode = None
            
            #curNode = curNode.next
            
        else:
            cur = self.head
            prev =None
            while cur.next !=self.head:
                prev = cur
                cur = cur.next
                if cur == curNode:
                    prev.next = cur.next
                    cur = cur.next

        
        
        return




    def josephus_problem(self,step):
      
        
        print("step",step)
        cur = self.head 
        while len(self) > 1:
            count =1
            while count != step:
                cur = cur.next
                count+=1
            print("Kill",cur.data)
            self.remove_node(cur)
            cur = cur.next
obj = CircularLinkedList()


obj.append("A")
obj.append("B")
obj.append("C")

obj.print_list()
obj.josephus_problem(1)
print("o/p")
obj.print_list()
# obj.split_list()
