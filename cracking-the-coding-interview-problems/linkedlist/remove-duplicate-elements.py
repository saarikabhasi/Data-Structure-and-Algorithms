"""
Remove duplicate elements from linkedlist

i/p:12->11->12->2->14->11->16->2->None
o/p: 12->11->2->14->16

"""


class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        
class simpleLL():
    def __init__(self) -> None:
        self.head =None
        self.size = 0

    def __is_list_empty(self):
        """
        while deleting we have to make sure that the list is empty. This function checks if the 
        linked list is empty
        """
        return self.head == None

    def insert_at_end(self,data):
        """
        function to insert a data at the end
        """
        newnode = Node(data)
        if not self.__is_list_empty():
            p = self.head
            while p.next:
                p = p.next
            p.next = newnode
        else:
            self.head = newnode

        self.size +=1
        
    def insert_at_begin(self,data):
        """
        function to insert a data at the begin
        """
        newnode = Node(data)
        if not self.__is_list_empty():
            newnode.next = self.head
            self.head = newnode
        else:
            self.head = newnode
        self.size +=1
    
    def insert_new_node_after_given_data(self,afterData,data):
        """
        function to insert a new node after the data
        """
        newnode = Node(data)
        if not self.__is_list_empty():
            p = self.head

            while  p and p.data !=afterData :
                p = p.next

            if p == None:
                print("cant find data")
            else:
                if p.next:
                    after = p.next
                    newnode.next = after

                p.next = newnode
        else:
            print("List empty")
            return
        self.size +=1
    
    def delete_node(self,node):
        """
        Delete given node
        
        """
        if node == self.head:
            #delete head node
            self.head = self.head.next
        elif node.next ==None:
            #last node
            p =self.head
            while p.next !=node:
                p= p.next 
            
            #make last second node point to None
            p.next = None
        else:
            #middle node
            p =self.head
            while p.next !=node:
                p =p.next
            p.next = node.next

        self.size -=1

    def show(self):
        p = self.head
        while p :
            print(p.data)
            p =p.next
        print("====================")
            
class remove_dups():
    def __init__(self,llobj) -> None:

        self = llobj
        


    def remove_dups_with_hash(self,lobj):
        """
        Remove duplicate item in unsorted list using hash

        Time: O(n)
        Space: O(N)        
        """
        self = lobj
        p = self.head 
        hash = dict()
        while p :
            if  p.data not in hash.keys():
                hash[p.data] = p.data
            else:
                self.delete_node(p)
            p = p.next
    
    def remove_dups_with_two_pointers(self,lobj):
        """
        Remove duplicate item in unsorted list using two pointer
        Time: O(n^2)
        Space: O(1)

        
        """
        self = lobj
    
        p1 = self.head
        if p1 == None or p1.next == None :
            return
        p2 =p1.next

        while p1.next != None and p2.next !=None:
            if p1.data !=p2.data:
                p2 =p2.next
            else:
                #delete p2
                self.delete_node(p2)
                p1 = p1.next
                p2 = p1.next
                
        


        

    
lobj = simpleLL()
lobj.insert_at_end(12)
lobj.insert_at_end(11)
lobj.insert_at_end(12)
lobj.insert_at_end(2)
lobj.insert_at_end(11)
lobj.insert_at_end(16)
lobj.insert_at_end(2)
lobj.insert_new_node_after_given_data(2,14)

lobj.show()

robj = remove_dups(lobj)
robj.remove_dups_with_hash(lobj)
lobj.show()

robj.remove_dups_with_two_pointers(lobj)
lobj.show()


       
            

            



            

  
            



