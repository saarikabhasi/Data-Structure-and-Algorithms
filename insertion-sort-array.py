"""
6 5 3 1 8 7 2 4
complexity = O(n^2)

"""
class Solution:
    def insertion_sort(self,a):
        n = len(a)
        if n==1:
            return a
        j = 1
        while j<n:
            for i in range(j,0,-1):
                if a[i]<a[i-1]:
                    t=a[i-1]
                    a[i-1]=a[i]
                    a[i] = t
            j=j+1
        return a


        

obj = Solution()
array = [6,5,3,1,8,7,2,4,]
print(obj.insertion_sort(array))
