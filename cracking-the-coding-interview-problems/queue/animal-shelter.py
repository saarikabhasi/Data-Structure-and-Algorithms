"""
cracking the coding interview page #99 problem #3.6
Solution 1:
Use Two queues: Dog & Cat, increment Priority(ranges from 1 till n; 1 is first one to be removed)
1. EnQ: 
    * enq to given type of animal Queue
    * increase Priority on each enQ
    * assign Priority to each node
2. deQany: 
    * check proirity of each animal queue
    * dequeue the node which has least priority
"""
class Node():
    def __init__(self,data) -> None:
        """
        create node
        
        """
        self.data = data
        self.next = None
        self.priority = None
class queueLL():
    def __init__(self) -> None:
        """
        create Queue
        """
        self.front = None
        self.rear = None
        

    def isEmpty(self):
        """
        checks if Q is empty
        
        """
        return self.front == self.rear==None
    
 
    def enQ(self,data,priority ):
        """
        enqueue data to the given obj
        increase Priority and assign  to node
        
        """
        newNode = Node(data)

        if self.isEmpty():
            self.front=newNode
            self.rear = newNode
            
        else:
            self.rear.next = newNode
            self.rear = newNode

        newNode.priority=priority
            
    def deQ(self):
        """
        dequeue data from the given object queue
        
        """
        if not self.isEmpty():
            t =self.front.data
            if self.front == self.rear:
                #single item
               
                self.front = self.rear = None
                
            else:
                self.front = self.front.next
        else:
            print("Empty")
        return t

    def display(self):
        """
        Show the Q
        
        """
        p =self.front
        if not p:
            print("Empty")
        while p:
            print(p.data)
            p = p.next
        
        
class animalShelter():
    def __init__(self) -> None:
        """
        create animal shelter
        total is the Priority counter


        """
        self.dog = queueLL()
        self.cat = queueLL()
        self.type = ["dog","cat"]
        self.total = 0

    def is_both_q_empty(self):
        """
        checks if  both queues are empty, 
        
        """
        return self.dog.isEmpty() and self.cat.isEmpty()

    def enqueue(self,data,type):
        """
        enQ items to given type Queue. Increase the total counter for each enQ operation

        """
        if type in self.type:
            self.total +=1
            if type == "dog":
                # dog enQ
                
                self.dog.enQ(data,self.total)
                
            elif type == "cat":
                #type cat enQ
                
                self.cat.enQ(data,self.total)
            

            
        else:
            print("Wrong type")
        return


    def dequeueAny(self):
        """
        DequeueAny animal from queue based on their priority
        case1: if both queues are empty then show message
        case2: if dog is empty, remove from cat
        case3: if cat is empty, remove from dog
        case4: compare Priorities between cat and dog, remove animal with least Priority 

        
        """
        if not self.is_both_q_empty():
            print("Dog and Cat empty")
            
            
            if self.dog.isEmpty():
                self.dequeueCat()
                
            elif self.cat.isEmpty():
                self.dequeueDog()
        

            else:
                if self.dog.front.priority < self.cat.front.priority:
                    self.dequeueDog()
                    
                else:
                    self.dequeueCat()
        else:
            print("Both cat and dog is empty")  
        return
    
    def dequeueDog(self):
        """
        Remove dog from dog q
        
        """
        d = self.dog.deQ()
        print("DeQed item",d, "from dog")
        if self.is_both_q_empty():
            self.total = 0

    def dequeueCat(self):
        """
        Remove dog from cat q
        
        """
        c = self.cat.deQ()
        print("DeQed item ",c,"from cat")
        if self.is_both_q_empty():
            self.total = 0

    def show(self,type):
        """
        Display the queues, according to type
        """
  
        if type=="dog":
            print(type)
            self.dog.display()
        elif type =="cat":
            print(type)
            self.cat.display()
        elif type =="both":
            print("dog")
            self.dog.display()
            print("cat")
            self.cat.display()
        else:
            print("Wrong type")

o = animalShelter()
o.enqueue("A","dog")
o.enqueue("B","cat")
o.enqueue("C","dog")
o.show("both")
o.dequeueDog()
o.show("both")
o.dequeueAny()
o.show("both")
o.dequeueAny()
o.show("both")
o.enqueue("A","dog")
o.show("dog")
o.dequeueAny()
o.show("both")
o.dequeueAny()
