"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true

Constraints:

0 <= c <= 231 - 1

"""


class Solution:
    def findsquarerootwithBST(self,c):
        l = 0
        r = c
        
        while l<r:
            m = (l+r) //2
            if m==l or m==r:
                if l**2 < c:
                    return l
                if r**2 < c:
                    return r
                
                
            if m**2>c:
                r = m
            elif m*m<c:
                l = m
            else:
                if m**2 == c:
                    return m
            
            
            
                
            
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0 or c == 1 :
            return True

        
        a =self.findsquarerootwithBST(c)
        
        
        i,j = 0,a
        while i<=j:
            r = i**2 + j **2
            
            if  r == c:
                return True
            elif r<c:
                i +=1
            else:
                j-=1
        return False
    
                
                
    
            
            
            
