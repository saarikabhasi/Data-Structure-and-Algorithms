"""
Cracking coding interview page #94 , question#2.3

Delete middle node: Write an algorithm to delete a node in the middle of a singly linked list
(not first or last node)

a->b->c->d->e
delete(c) 
a->b->c->d->e

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

    def return_kth_position_node(self,k):
        """


        """
        p = self.head
        if not p:
            return "list empty"
             
        elif k <=0:
            return "k size begins with 1"
        if k == 1:
            return p
        else:
            pos = 1
            while p and pos != k:
                pos +=1
                p = p.next
            if p is None and pos !=k:
                return 'position not found'

            return p

   
class delete_middle_node(simplelinkedlist):

    def __init__(self,obj) -> None:
        super().__init__()
        self = obj
    def delete_middle_node(self,obj,node):
        print("Given node",node.data)
        self = obj
        if node == self.head or node.next ==None:
            return 'Can\'t delete first or last node'
        else:
            p=self.head
            prev = p
            while p.next and p !=node :
                prev = p
                p = p.next 
            
            prev.next = node.next
            
        return 'Deleted the node'
            
    

obj = simplelinkedlist()
obj.insert_data_at_end("a")
obj.insert_data_at_end("b")
obj.insert_data_at_end("c")
obj.insert_data_at_end("d")
obj.insert_data_at_end("e")



dobj = delete_middle_node(obj)
node = obj.return_kth_position_node(5) 
print(dobj.delete_middle_node(obj,node)  ) 
obj.show()