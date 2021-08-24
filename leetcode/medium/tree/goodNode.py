# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
target = root.val //constant

root node's value is the least maximum number, all other child node's value must be greater than or equal to this number and it's root value to be considered to be good nodes




"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes_count =1
        
        goodNodes_count= self.helper(root.left,root.val,root.val,root.val,goodNodes_count)
        goodNodes_count= self.helper(root.right,root.val,root.val,root.val,goodNodes_count)
        
        return goodNodes_count
    
    def helper(self,node,leastMax, rootValue,currentMax,goodNodes_count):
        
        if node ==None:
            return goodNodes_count
        
        if node.val>= leastMax and node.val>=rootValue and node.val>=currentMax:
            currentMax = node.val
            goodNodes_count+=1
  
        
        path= self.helper(node.left,leastMax,node.val,currentMax,path)
        path = self.helper(node.right,leastMax,node.val,currentMax,path)
        return goodNodes_count
            
                
            
        
        
       
