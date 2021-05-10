"""
Given an array of n distinct integers sorted in ascending order, 
write a function that returns a Fixed Point in the array,
if there is any Fixed Point present in array, else returns -1.
Fixed Point in an array is an index i such that arr[i] is equal to i. 
Note that integers in array can be negative. 

Examples: 
 

  Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3 

  Input: arr[] = {0, 2, 5, 8, 17}
  Output: 0  // arr[0] == 0 


  Input: arr[] = {-10, -5, 3, 4, 7, 9}
  Output: -1  // No Fixed Point
 

"""
def find_fixed_num(arr):

    def fixed_num(a,p):
        n = len(a)
        if n <=0:
            return -1
        m = n//2 
        if a[m] == m+p: 
            return a[m]
        elif a[m] < m+p :
            return fixed_num(a[m+1::],m+1)
        else:
            if a[m]>m+p:
                return fixed_num(a[0:m],p)



    return fixed_num(arr,0)

    

print(find_fixed_num([-1, 0, 2, 5, 7, 9]))
