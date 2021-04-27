"""
A -> B ->C -> None

head_pointer = A

Insert
------
    1. insert_at_end
    2. insert_at_beginning
    3. insert_after_node

Delete
-------
Delete by value:
    1. delete head element 
    2. delete a element that is not head
Delete at a  position:
    1. delete node at position at 0
    2. delete node at position other than 0

Length
_______

Find length of list list
1. iterative approach
2. recursice approach

Swap
_____
1. One of the nodes is a head node.
2. Both nodes are not head node
steps:
1. Find keys and previous node  
2. swap the keys and create the link using previous node pointer

Reverse nodes
------------
1. arrows are flipped to reverse the pointers
2. Iterative and recursive approach

Merge two sorted linked list
____________________________
Algorithm:

Three pointer p,q,s
p points to list1, q points to list2, s points to smaller number between p and q

border conditions:
1. if any of the list is empty, return non empty list

headstart: 
1. to begin with first assign s with either p or q
2. make s point to smaller number between p and q
3. make p or q point to next number of s

in loop repeat until either p or q is none
1. compare p and q
2. make s point to smaller number betwenn p and q
3. make p or q point to next number of s

End condition after loop
1. After loop, check which pointer p or q is pointing to none. make s point to that pointer 
2. make self.head point to new head


Print nth node from last
_________________________

first solution:

1. find length of list
2. decrement the total length by one untill the cur pointer is at nth node

second solution:

1. two pointer p and q
2. place p in head and q in nth steps after p
3. increment p and q by one until q is none
4. When q is none return p (p will be nth node from last)

Count occurence
_________________
Find the number of occurence of given value in a list

two approaches: iterative & recursive

iterative:
1. loop till the cur_node reaches none
    i. if cur_node.data is given value, increment count by 1
return count

recursive:
base: none is node
node = node.next
return 1 + function_call(node,data)

Rotate after a pivot:
______________________

1. Rotate elements after a pivot
example: 1->2->3->4->5
pivot : 3
result: 4->5->1->2->3->None

Algorithm:
p points to pivot, q to last element

q.next = self.head
self.head = p.next
p.next = None


Palindrome:
___________

Check if a linked list is a palindrome

3 approaches: 
1. using string
2. Stack
3. 2 pointers

"""

class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):

        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node =cur_node.next
        print("_______________")
        
    def insert_at_end(self,data):
        print("insert_at_end")
        #create new node
        new_node = Node(data)
        #empty linked list
        if self.head is None:
            self.head = new_node
            return
        # find last node and link new node to last node
        last_node = self.head
        while last_node.next:
            last_node  = last_node.next
        last_node.next = new_node
        return

    def insert_at_beginning(self,data):
        print("insert_at_beginning")
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        next_node =self.head
        self.head = new_node
        new_node.next = next_node

    def insert_after_node(self,afterdata,newdata):
        print("insert_after_node")
        new_node = Node(newdata)

        cur_node = self.head
        if self.head is None:
            print("List is empty")
            return
        # check if afterdata exist in list
        while cur_node.next and cur_node.data!=afterdata:
            cur_node =cur_node.next
        # afterdata does not exist in 
        if cur_node.data == afterdata:   
            next_node = cur_node.next 
            new_node.next = next_node
            cur_node.next = new_node

    #delete
    def delete_node(self,data):
        print("delete node",data)
        if self.head == None:
            print("list empty")
            return
        # del head data    
        if self.head.data == data:
            self.head = self.head.next 
        # del data that is not head
        cur_node = self.head
        prev_node = None
        while cur_node.next and cur_node.data!=data:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node.data == data:
            prev_node.next = cur_node.next
            cur_node = None
        
    def delete_node_at_pos(self,pos):
        print("delete_node_at_pos",pos)
        if not self.head:
            print("List empty")
        if pos <= 1 and self.head:
           self.head=self.head.next
        cur_node = self.head
        size = 1
        prev_node = cur_node
        while cur_node.next and size != pos:
            size+=1
            prev_node= cur_node
            cur_node = cur_node.next
            
        if size == pos:
            prev_node.next = cur_node.next
            cur_node = None
    
    def len_iterative(self):
        cur_node = self.head
        size = 0 
        if not cur_node:
            print("Length of list:",size)
            return
        
        while cur_node.next:
            size+=1
            cur_node = cur_node.next
        print("Length of list:",size+1)
        return

    def len_recursive(self,node):
        if node == None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self,v1,v2):
        print("swap:",v1,"and",v2)
        if self.head == None:
            return 
        if v1 == v2:
            return 
        # find v1 and v2 position

        #find v1 
        cur_node_v1 = self.head
        prev_node_v1  = None
        while cur_node_v1.next:
            if cur_node_v1.data == v1:
                break
            prev_node_v1 = cur_node_v1
            cur_node_v1 = cur_node_v1.next

        #find v2
        cur_node_v2 = self.head
        prev_node_v2 = None
        while cur_node_v2.next:
            if cur_node_v2.data == v2:
                break
            prev_node_v2 = cur_node_v2
            cur_node_v2 = cur_node_v2.next


        if not cur_node_v1.data == v1 or not cur_node_v2.data == v2:
            return

        #swap
        if prev_node_v1:
            prev_node_v1.next = cur_node_v2
        else:
            self.head = cur_node_v2
        if prev_node_v2:
            prev_node_v2.next = cur_node_v1
        else:
            self.head = cur_node_v1
        cur_node_v1.next,cur_node_v2.next  = cur_node_v2.next,cur_node_v1.next

    def reverse_iterative(self):
        cur = self.head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev
    
        
    def reverse_recursive(self):
        def _reverse_recursive(cur,prev):
            if cur == None:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur,prev)
        self.head = _reverse_recursive(self.head,None)
    
    def merge_sorted(self,list2):
        p = self.head
        q = list2.head
        s = None

        #border condition
        if not p:
            return q
        if not q:
            return p 

        #make s point to p or q before loop begins
        if p and q:
            if p.data<=q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        # loop
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next 
        #end condition
        if not p:
            s.next = q
        if not q:
            s.next = p
        self.head = new_head

        return self.head

    def remove_duplicates(self):
        cur = self.head
        h = dict()
        
        while cur:
            if cur.data not in  h.keys():
                h[cur.data] = cur.data
                prev = cur
            else:
                prev.next = cur.next
                cur = cur.next
    
    def print_nth_node_from_last(self,n,method):
        if method == 1:
            cur = self.head
            l = self.len_recursive(self.head)
            while cur:
                if l == n:
                    return cur.data
                l = l-1
                cur = cur.next
            if cur == None:
                return

        if method == 2:
            p = self.head
            q = self.head
            pos = 0
            if n>0:
            
                while  q:
                    if pos >= n:
                        break
                    pos +=1
                    q = q.next
                
                if not q:
                    print(n, "is greater length of list",self.len_recursive(self.head))
                    return

                while q is not None:
                    q = q.next
                    p = p.next
                
                if q == None:
                    return p.data
      

            else:
                return None
        
    def count_occurences_iterative(self,data):
        cur = self.head
        count=0
        while cur:
            if cur.data == data:
                count+=1
            cur = cur.next
        return count

    def count_occurences_recursive(self,node,data):
        
        if node is None:
            return 0
        if node.data == data:
            return 1+ self.count_occurences_recursive(node.next,data)
        else:
            return self.count_occurences_recursive(node.next,data)

    def rotate(self,pivot):
        cur = self.head
        if cur is None:
            return
        p = None
        q = None
        while cur:
            if cur.data == pivot:
                p = cur
                break
            cur = cur.next
        if cur:
            while cur:
                if cur.next == None:
                    q = cur
                cur = cur.next
        else:
            return
        #algorithm

        q.next = self.head
        self.head = p.next
        p.next = None
        return
    
    def is_palindrome_pointers(self):
        
        if self.head:
            p = self.head
            q = self.head
            prev = []
            i = 0
            while q:
                prev.append(q)
                q = q.next
                i+=1
                
            q=prev[i-1]

            count = 1
            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True



        
             
        

listobj = LinkedList()
listobj.len_iterative()
listobj.insert_at_end("A")
listobj.len_iterative()
listobj.insert_at_end("B")
listobj.insert_at_end("C")
listobj.print_list()
listobj.insert_after_node("B","D")
listobj.print_list()
listobj.delete_node("B")
listobj.print_list()
listobj.insert_at_end("E")
listobj.print_list()
listobj.delete_node_at_pos(3)
listobj.insert_at_end("D")
listobj.insert_at_end("F")
listobj.print_list()
listobj.len_iterative()

print("Length of list:",listobj.len_recursive(listobj.head))
listobj.print_list()
#listobj.swap_nodes("A", "F")
listobj.reverse_iterative()

listobj.print_list()

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.insert_at_end(1)
llist_1.insert_at_end(5)
llist_1.insert_at_end(7)
llist_1.insert_at_end(9)
llist_1.insert_at_end(10)

llist_2.insert_at_end(2)
llist_2.insert_at_end(3)
llist_2.insert_at_end(6)


llist_1.merge_sorted(llist_2)
llist_1.print_list()

llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(1)
llist.insert_at_end(1)
llist.insert_at_end(1)
llist.insert_at_end(1)
llist.insert_at_end(1)
llist.insert_at_end(1)

print("Original Linked List")
llist.print_list()
print("Linked List After Removing Duplicates")
llist.remove_duplicates()
llist.print_list()
llist = LinkedList()
llist.insert_at_end("A")
llist.insert_at_end("B")
llist.insert_at_end("C")
llist.insert_at_end("D")
# print(llist.print_nth_node_from_last(1,2))
    
    
llist_2 = LinkedList()
llist_2.insert_at_end("A")
llist_2.insert_at_end("B")
llist_2.insert_at_end("A")
# print(llist_2.count_occurences_iterative(4))
# print(llist_2.count_occurences_recursive(llist_2.head, 1))
# llist_2.print_list()
# llist_2.rotate("A")
# llist_2.print_list()
print(llist_2.is_palindrome_pointers())
        

