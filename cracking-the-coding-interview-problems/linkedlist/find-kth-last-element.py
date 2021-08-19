"""
Cracking coding interview page #94 , question#2.2
Find kth last element of a single linked list
1->2->3->4->5

k= 6, return False
k=5, return 1
k= 3, return 3
k=2, return 4
k = 1, return 5

Approach 1 : With size  
        step1 : find the size of list
        step2 : return data present in (size -k) +1th position
        The idea is to increment the pointer from head till the given position

Approach 2: With pointers

        step 1: p1 points to head and p2 points k times far node
        step 2: increment p1 and p2  untill p2 reaches end of list

        The idea is to place first pointer(p1) on head and second pointer(p2) k times far from head
        On each step, move both pointer to next node until p2 reaches end of list

        return first pointer as first pointer to pointing to kth last node

Find kth last node and delete that node

        step 1: p1 points to head and p2 points k times far node
        step 2: increment p1 and p2  untill p2 reaches end of list

        The idea is to place first pointer(p1) on head and second pointer(p2) k times far from head
        On each step, move both pointer to next node until p2 reaches end of list

        return first pointer as first pointer to pointing to kth last node


"""
class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class simplelinkedlist():
    def __init__(self) -> None:
        self.head = None

    def insert_data_at_begin(self,data):
        """
        insert a data at the begining
        
        """
        node = Node(data)
        if self.head==None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
    def insert_data_at_end(self,data):
        """
        insert a data at end of list
        
        """
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            p = self.head
            while p.next:
                p =p .next
            p.next = node
    def insert_data_at_a_position(self,data,pos):
        """
        insert data at given position
        """
        
        if self.head == None:
            print("List empty")
            return 
        else:
            c = 0
            p = self.head

            while p.next:
                c +=1
                if c == pos:
                    break
                p = p.next
            
            if c == pos:
                node = Node(data)
                node.next = p.next
                p.next = node
            else:
                print("Cant find pos")
        return
    def insert_data_after_a_node(self,data,node):
        """
        insert data after the given node
        
        """
        newnode = Node(data)
        if self.head == node:
            node.next =self.head.next
            self.head.next = node
        elif self.head == None:
            print("List empty")
            
        else:
            p  =self.head
            while p !=node:
                p = p.next
            
            newnode.next = p.next
            p.next = newnode
        return
    
    def delete_given_node(self,node):
        """
        delete given node
        """
        if self.head == None:
            return "List is empty"
        elif self.head == node:
         
            self.head = self.head.next
            
        else:
            p =self.head
            while p.next != node:
                p = p.next
            p.next =node.next
        
        return 
        
    def delete_node_at_position(self,pos):
        """
        delete node at given position
        """
        if self.head == None:
            print("List empty")
        elif pos == 1:
            self.head = self.head.next
        else:
            p = self.head 
            c = 1

            prev = None
            while p and c !=pos :
                prev = p
                p = p.next
                c+=1
            
            if p!=None and prev != None:
                prev.next = p.next
            else:
                print("postion not found\n--------------------")

        return
            

    def delete_data(self,data):
        """
        Delete the first occurence of data from list
        
        
        """
        if self.head == None:
            print("List empty")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            p =self.head 
            prev = None
            while p and p.data != data :
                prev = p
                p =p.next
            if prev and p:
                prev.next = p.next
            else:
                print("cant find the data")
        return
    
    def show(self):
        p =self.head
        if not p:
            print("Empty list")
        else:
            while p:
                print(p.data)
                p = p.next
        print("_____________________")
            

class kth_last_element(simplelinkedlist):
    def __init__(self) -> None:
        super().__init__()
        
    def insert_data_after_a_node(self, data, node):
        return super().insert_data_after_a_node(data, node)
    def insert_data_at_a_position(self, data, pos):
        return super().insert_data_at_a_position(data, pos)
    def insert_data_at_begin(self, data):
        return super().insert_data_at_begin(data)
    def insert_data_at_end(self, data):
        return super().insert_data_at_end(data)
    def delete_data(self, data):
        return super().delete_data(data)
    def delete_given_node(self, node):
        return super().delete_given_node(node)
    def delete_node_at_position(self, pos):
        return super().delete_node_at_position(pos)
    def show(self):
        return super().show()

    def show_kth_last_element_with_size(self,k):
        """
        Approach 1 : With size  
        step1 : find the size of list
        step2 : return data present in (size -k) +1th position
        The idea is to increment the pointer from head till the given position

        

        """
        size = 0

        p =self.head

        while p:
            size+=1
            p =p.next

        
        if size == 1:
            return  "list empty"

        elif k>size:
            print("given kth number is greater than total size of list")
        elif k<=0:
            return "k size begins with 1"
        else:
            pos = 1
            p =self.head
            while p and pos != (size-k)+1:
                pos +=1
                p =p.next
            return p.data
         
    def show_kth_last_element_with_pointers(self,k):
        """
        Approach 2: With pointers

        step 1: p1 points to head and p2 points k times far node
        step 2: increment p1 and p2  untill p2 reaches end of list

        The idea is to place first pointer(p1) on head and second pointer(p2) k times far from head
        On each step, move both pointer to next node until p2 reaches end of list

        return first pointer as first pointer to pointing to kth last node


        """
        p1 = self.head
        if not p1:
            return "list empty"
             
        elif k <=0:
            return "k size begins with 1"

        else:
            pos = 1
            p = self.head
            while p and pos != k:
                p = p.next
                pos +=1
            p2 = p
            if p2 == None:
               return "k is greater than overall list size"
            else:
                while p2.next:
                    p1 =p1.next
                    p2 =p2.next
                return p1.data
   
    def find_and_delete_kth_last_node_with_pointers(self,k):

        """
        Find kth last node and delete that node

        step 1: p1 points to head and p2 points k times far node
        step 2: increment p1 and p2  untill p2 reaches end of list

        The idea is to place first pointer(p1) on head and second pointer(p2) k times far from head
        On each step, move both pointer to next node until p2 reaches end of list

        return first pointer as first pointer to pointing to kth last node


        """
        p1 = self.head
        if not p1:
            print("List empty") 
        elif k<=0:
            print("kth index must be greater than or equal to 1") 
        else:
            p2 = p1
            pos = 1

            while p2 and pos != k:
                pos +=1
                p2 = p2.next

            if p2 == None:
                print('k is greater than overall size') 
            else:
                while p2.next:
                    p1 =p1.next
                    p2 = p2.next
                self.delete_given_node(p1)
            
        return 
         
    
kobj = kth_last_element()
kobj.insert_data_at_end(2)
kobj.insert_data_at_begin(1)
kobj.insert_data_at_end(4)
kobj.insert_data_at_end(5)
kobj.insert_data_at_a_position(3,2)
kobj.show()

print(kobj.show_kth_last_element_with_pointers(1))
print(kobj.show_kth_last_element_with_size(1))
print("-------")
kobj.find_and_delete_kth_last_node_with_pointers(6)
kobj.show()

kobj.delete_data(6)
kobj.show()

                


        
            
            
            