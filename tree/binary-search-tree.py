"""
Binary Search Tree: Binary tree arranged according to binary search property. 

Example:
            8
           / \
          3   10
        /  \    \
       1    6     14
           / \    /
          4   7  13
Operations:
1. Insertion
2. Insertion of reverse sorted list
3. Search
4.is_bst_satisfied : check if tree is BST

"""
class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self,root):
        self.root = Node(root)
    
    def insert(self,new_val):
        self.insert_helper(self.root,new_val)

    def insert_helper(self,current,value):
        if value <current.value:
            if current.left:
                self.insert_helper(current.left,value)
            else:
                current.left = Node(value)
        else: 
            if current.right:
                self.insert_helper(current.right,value)
            else:
                current.right = Node(value)

        return 

        
        
    def search(self,value):
        return self.search_helper(self.root,value)

    def search_helper(self,current,value):
        if current:
            if current.value == value:
                return True
            elif value < current.value:
                return self.search_helper(current.left,value)

            else: 
                return self.search_helper(current.right,value)
            
        return False
            
    def is_bst_satisfied(self):    
        def helper(node,lw=float('-inf'),mx=float('inf')):
            if not node:
                return True
            val = node.value

            if val <= lw:
                return False
            if val> mx:
                return False

            if not helper(node.left,lw,val):
                return False
            if not helper(node.right,val,mx):
                return False
            return True


        
        return helper(self.root)


                

            
        


bst = BinarySearchTree(8)    
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)

# print(bst.search(19))

bst = BinarySearchTree(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

# print(bst.search(9))
# print(bst.search(14))
print(bst.is_bst_satisfied())
