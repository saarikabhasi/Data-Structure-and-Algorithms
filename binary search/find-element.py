"""
find if element exist in array using binary search
"""
def binary_search(arr, target):
    n = len(arr)
    mid = n//2

    if n == 1 and arr[0] == target:
        return True
    if n >1:
        if arr[mid] == target:
            return True
        elif target > arr[mid]:
            return binary_search(arr[mid::],target)
        else:
            return binary_search(arr[0:mid],target)
    return False
   


array =  [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 33
print(binary_search(array,target))