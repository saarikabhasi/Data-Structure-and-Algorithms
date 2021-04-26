"""

-2, 1, 2, 4, 7, 11
Given an array of integers, return True or False if the array has two numbers that add up to a specific target. 
You may assume that each input would have exactly one solution.
(2,11) - True

Algo:

1. Hashing: 
    i. Push array values in dict - O(n)
    ii.Loop from i=0 till i<sizeof array-1 O(n)
        sub = Target - dict.key[i] O(1)
        check if sub exist as key in dict.O(n)
        if exists return the (i, sub)and True
        else return False
    iii. Complexity- O(n)
2. Two pointer Technique: Assumes list is sorted in ascending order
    i. l points to first element and r points to last element
    ii. check if A[l]+A[r]<target
        move l to right by one step if true
        else: move r to left by one step 
    iii. return True if Target is found
    iv. return False when r is larger than l 
    v. Complexity - O(n)
    
"""
def two_sum_hashing(A,target):
    # O(n) Complexity
    A_hash = dict()
    i = 0
    n = len(A)
   
    for val in A:
        A_hash[val] = True

    while i<n:

        sub = target+A[i]
        if sub in A_hash:
            return True
        i +=1
    return False

def two_sum_pointer(A,target):
    n = len(A)
    l = 0
    r = n-1
    while l < r:
        if A[l]+A[r]<target:
            l+=1
        elif A[l]+A[r] == target:
            return True
        else:
            r-=1
    return False
A = [-2, 1, 2, 4, 7, 11]
target = 13000
print(two_sum_hashing(A,target))
print(two_sum_pointer(A,target))