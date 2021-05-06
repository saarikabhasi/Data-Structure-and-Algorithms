"""

Given a sorted array, find a number in array that is closest to the target number.

Example:
Input :
    arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
    Target number = 11
    Output : 9
    9 is closest to 11 in given array
Input :
    arr[] = {2, 5, 6, 7, 8, 8, 9};
    Target number = 4
    Output : 5
"""

def closest_number(arr,target):
    
    def find_closest_num (arr):
        n = len(arr)
        m = n//2
        if n == 1:
            return arr[0]

        if m-1 >=0 and m +1 < n:
            if abs(target - arr[m-1]) < abs(target - arr[m+1]):
                return find_closest_num(arr[0:m])
                
            else:
                return find_closest_num(arr[m:n])
        else:
    
            if abs(target - arr[m]) < abs(target - arr[0]):
                return find_closest_num(arr[m::])
            return find_closest_num(arr[0:m])


    return find_closest_num(arr)
  

# arr = [1, 2, 4, 5, 6, 6, 8, 9]
# target=7
arr = [2, 5, 6, 7, 8, 8, 9]
target = 4
print(arr)
print("T",target)
print(closest_number(arr,target))