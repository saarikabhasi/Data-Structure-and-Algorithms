#Find a peak element in a 2D array

class Solution:  
    v=0
    
    def findMax(self,nums):
        n = len(nums)
        mid = int(n/2)
        if n==1:
            return self.v
        
        if n>=2:
            if nums[n-1]>nums[n-2]:
                self.v += n-1
                return self.v
            if nums[0]>nums[1]:
                return self.v
            
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            self.v += mid
            return self.v
        
        if nums[mid-1]>nums[mid]:
            self.v+=0
            return self.findMax(nums[0:mid])
        if  nums[mid+1]>nums[mid]:
            self.v += mid
            return self.findMax(nums[mid::])
        
    def findPeakElement(self, array,row,col):
        print(array)
        #find middle row
        mid = int(row/2)
        # find peak of that row
        
        
        ind_j = self.findMax(array[mid])
        print(ind_j)
        element1 = array[mid][ind_j]
        print(ind_j,element1)
        column = [r[ind_j] for r in array]
        # find peak of that column
        self.v =0 
        ind_i = self.findMax(column)
        element2 = array[ind_i][ind_j]
        print(ind_i,ind_j,element2)
        if element1 == element2:
            print("result",element1) 
        elif element1>element2:
            print("result",element1) 
        else:
            self.v =0 
            column = [r[ind_j] for r in array]
            self.findMax(column)



sol = Solution()
 
# a = ([[1,2,1000],
#     [1,6,4],
#     [7,16,0]])
a = ([[10,7],
    [11,17]])

a = ([10, 8, 10, 10 ], 
    [14, 13, 12, 11 ], 
    [15, 9, 11, 21 ], 
    [16, 17, 19, 20 ] ); 
  
sol.findPeakElement(a,4,4)
