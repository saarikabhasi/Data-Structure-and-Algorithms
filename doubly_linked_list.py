"""
None<->A->B<->C<->None
Head = A

1. Print list
2. Append Node (at end)
3. Prepend Node (at beginning)
4. Add Node at a position
5. Add Node Before/After given key
6. Delete given key (removes first occurence of key in the list)
    i. delete only node
    ii. delete head node but the only node
    iii. delete node in middle
    iv. delete last node

7. Reverse list
8. Remove duplicates
9. Delete nodes :delete given node 
10. pair with sum

"""
class Node:

    def __init__(self,data):
        self.data  = data
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
    
    def print_list(self):
        cur =self.head
        if not cur:
            print("List empty")
        while cur:
            print(cur.data)
            cur = cur.next
        print("______________")
    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_node_at_a_position(self,data,position):
        # add data at a position

        new_node = Node(data)
        count = 0

        if not self.head:
            # list is empty
            self.append(data)
            return
        if position == 1 or position == 0: 
            # insert at head
            self.prepend(data)
            return
        cur = self.head
        new_node = Node(data)
        while cur:
            count +=1
            if count == position:
                # prepend data at middle
                new_node.next = cur
                new_node.prev =cur.prev
                cur.prev.next = new_node
                cur.prev = new_node
                return
            cur = cur.next
        # insert at end    
        self.append(data)

    def add_after_node(self,key,data):
        #add data after the key
        print("add ",data,"after ",key)
        if not self.head:
            print("List is empty, appending anyway")
            self.append(data)
            return
        cur = self.head
        new_node = Node(data)
        while cur:
            if cur.data == key:
                new_node.next = cur.next
                cur.next = new_node
                new_node.prev = cur
                if cur.next is not None:
                    # Key is not last node
                    cur.next.prev = new_node
                return
                
            cur = cur.next
        
        
        print("key not found")
            
    def add_before_node(self,key,data):
        #add data before the key
        print("Add ",data, "before",key)
        cur = self.head
        if self.head is None or cur.data is key:
            self.prepend(data)
            return
        
        new_node = Node(data)
        while cur:
    
            if cur.data is key:
 
                new_node.next = cur
                new_node.prev = cur.prev
                cur.prev.next = new_node
                cur.prev = new_node
                return
            cur = cur.next

    def delete_key(self,key):
        print("Delete node",key)
        cur = self.head
        # make sure we are not deleting an empty list
        if not cur:
            print("List is empty")
            return
        # case i: delete only node
        if cur.next is None:
            if cur.data is key:
                print("delete only node")
                self.head = None
                cur = None
                return
            print("Key not found") 
            return
        # case ii: delete head node
        else:
            # key is the head node, but not the only node
            if cur.data is key:
                print ("key is the head node, but not the only node")
                self.head = cur.next
                cur.next.prev = None
                cur = None
                return
        #case iii: delete node in middle
        while cur.next:
            # key is in the middle, but not the last node
            if cur.data is key and cur.next : 
                print("key is the middle, but not the last node")
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur = None
                return
            cur = cur.next
        # case iv:  delete last node
        # key is the last node. 
        if cur.data is key and not cur.next:
            print("Key is the last node")
            cur.prev.next = None
            cur.prev = None
            cur = None
            return
        print("key not found in the list")

    def reverse(self):

        if not self.head:
            print("List is empty,Cannot reverse")
            return
        
        cur = self.head
        if cur.prev is None and cur.next is None:
            # first and only node
            print ("List has only one node")
            return 
        tmp = None
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
            if tmp:
                self.head = tmp.prev
                print("self.head",self.head.data)
             

        cur = self.head

    def remove_duplicates(self):
        cur = self.head

        duplicate = dict()
        while cur:
            
  
            if cur.data in duplicate.keys():
                duplicate[cur.data] +=1
            else:
                duplicate[cur.data] = 0

            if cur.data in duplicate.keys() and duplicate[cur.data] >=1:
                #delete 
                prev = cur.next
                self.delete_node(cur)
                cur = prev
            else:
                cur = cur.next
           


    def delete_node(self, node):

        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

                # Case 2:
                else:
               
                    nxt = cur.next
                    cur.next = None 
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur == node:
                # Case 3:
           
                if cur.next:
                    nxt = cur.next 
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None 
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
               
                    prev = cur.prev 
                    prev.next = None 
                    cur.prev = None 
                    cur = None 
                    return 
            cur = cur.next
    def pairs_with_sum(self, sum_val):  
        # 1->2->3->4->5 (pair added up to 5) 
        # ans: ["(1,4)","(2,3)"]
        cur = self.head
        output = []
        while cur:
            nxt = cur.next
            while nxt:
                if cur.data + nxt.data == sum_val:
                    pair = "("+str(cur.data)+","+str(nxt.data)+")"
                    output.append(pair)
                nxt = nxt.next
            cur=cur.next
        return output
obj = DoublyLinkedList()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
# 8->4->4->6->4->8->4->10->12->12
# obj.append("D")
obj.print_list()
# obj.add_node(1,"D")
# obj.print_list()
# obj.add_node(2,"D")
# obj.print_list()
# obj.add_node(3,"D")
# obj.print_list()
#obj.add_node_at_a_position("D",0)
#obj.add_after_node("C","D")
#obj.add_before_node("B","D")
#obj.delete_key("C")
#obj.print_list()
#obj.reverse()
# print(obj.remove_duplicates() )
#obj.print_list()
obj.print_list()
print(obj.pairs_with_sum(5))