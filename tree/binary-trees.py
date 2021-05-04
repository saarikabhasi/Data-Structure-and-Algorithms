"""
Binary Tree:


        1
      /   \
     2     3
    / \   / \
   4   5  6  7

1. Root: is the first node of the tree
2. Leaf Nodes: Nodes with 0 children/successors
3. Relationships :Node 1 is the grandparent of node 4 whereas node 4 is the grandchild of node 1
4. Ancestor:All the node on the path from node 4 till node 1 is considered at anscestor.
    For ex: Node 2 and 1 are the ancestors of node 4

5. Depth of tree: The of the path from a node to root node is depth. The depth of root is 0.
    Example: 
        1       - depth 0
      /   \
     2     3    - depth 1
    / \   / \
   4   5  6  7  - depth 2
      / \ 
     8   9      - depth 3

6. Height of the tree: The length of the path from n to its deepest descendent. 

    height of the tree = height of root node
    height of leaf node = Always 0
    
    Example:  Height of tree = height of root node = 3 , height of leaf node is 0

        1      
      /   \
     2     3    
    / \   / \
   4   5  6  7  
      / \ 
     8   9 
7. Complete Binary Tree: Except the last level, all the nodes are complete.
    And all the nodes in the last level are as far left as possible

    Example:

        1      
      /   \
     2     3    
    / 
   4     

8. Full Binary Tree: All nodes has exactly 0 or 2 children

    Example:
        1
      /   \
     2     3
    / \   / \
   4   5  6  7

9. Traversal:
    i. Pre-order: Root-> Left->Right (+ a b)
    ii. In-order : Left->Root->Right (a + b)
    iii. Post-order : Left->Right->Root (a b +)

    iv. Level order : print values level wise

        Example: o/p  1,2,3,4,5,6,7

               1
             /   \
            2     3
           / \   / \
          4   5  6  7
        Implementation: Using Queue
        loop1: 1            o/p= 0
        loop2: 2,3          o/p= 1
        loop3: 3,4,5        o/p= 1->2
        loop4: 4,5,6,7      o/p= 1->2->3
        loop5: 5, 6, ,7     o/p= 1->2->3->4
        loop6: 6, 7         o/p= 1->2->3->4->5
        loop7 : 7           o/p= 1->2->3->4->5->6
        loop 8: -           o/p= 1->2->3->4->5->6->7

    v. Reverse Level order: print nodes in reverse
        Example: o/p  4,5,6,7,2,3,1

               1
             /   \
            2     3
           / \   / \
          4   5  6  7
10. Height of Tree
11. Size of Tree

    
"""
class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self,value):
        return self.items.append(value)
        
    
    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def print_queue(self):
        print(self.items)

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self,value):
        return self.items.append(value)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

class Node(object):
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.pre_order(self.root,"")+ "None"
        if traversal_type == "inorder":
            return self.in_order(self.root,"")+ "None"
        if traversal_type == "postorder":
            return self.post_order(self.root,"") + "None"
        if traversal_type == "levelorder":
            return self.level_order(self.root,"") + "None"
        if traversal_type == "reverselevelorder":
            return self.reverse_level_order(self.root, "") +"None"

    def pre_order(self,start,output):
        if start:
            output += str(start.value)+"->"
            output = self.pre_order(start.left,output)
            output = self.pre_order(start.right,output)
        return output

    def in_order(self,start,output):
        if start:
            output = self.in_order(start.left,output)
            output += str(start.value) + "->"
            output = self.in_order(start.right,output)
        return output

    def post_order(self,start,output):
        if start:
            output = self.post_order(start.left,output)
            output = self.post_order(start.right,output)
            output += str(start.value) + "->"
        return output

    def level_order(self,start,output):
        
        q = Queue()

        if start:
            q.enqueue(start)

        while q.size()>0:
          
            output += str(q.peek().value)+"->"
            
            deQ = q.dequeue()
            if deQ.left:
                q.enqueue(deQ.left)
            if deQ.right:
                q.enqueue(deQ.right)

        return output
    
    def reverse_level_order(self,start,output):

        q = Queue()
        s = Stack()
        if start: 
            q.enqueue(start)
        
        while q.size()>0:
            deQ = q.dequeue()
            s.push(deQ.value)

            if deQ.right:
                q.enqueue(deQ.right)

            if deQ.left:
                q.enqueue(deQ.left)
      
        while not s.is_empty():
            output += str(s.peek()) + "->"
            s.pop()

        return output

    def height_of_tree(self,start):

        
        if start is None:
            return -1
        left_height = self.height_of_tree(start.left)
        right_height = self.height_of_tree(start.right)
        return max(left_height,right_height)+1
    
    def size_of_tree(self,start):
        if start is None:
            return 0
        else:
            return 1 + self.size_of_tree(start.left) + self.size_of_tree(start.right)



tree = BinaryTree('F')
tree.root.left = Node('B')
tree.root.right = Node('G')
tree.root.left.left = Node('A')
tree.root.left.right = Node('D')
tree.root.left.right.left = Node('C')
tree.root.left.right.right = Node('E')
tree.root.right.right = Node('I')
tree.root.right.right.left = Node('H')



print("pre-order",tree.print_tree("preorder"))
print("in-order",tree.print_tree("inorder"))
print("post-order",tree.print_tree("postorder"))
print("level order",tree.print_tree("levelorder"))
print("reverse level order",tree.print_tree("reverselevelorder"))
print("height of tree",tree.height_of_tree(tree.root))
print("size of tree",tree.size_of_tree(tree.root))




