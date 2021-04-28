"""
Given two sorted arrays, A and B, determine their intersection. 
What elements are common to A and B?

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

Soln 1: (Not implemented)

nlogm (n is the length of A and logm because we are doing a binary search in B)
Take i from 0 till len(A)
j is the midpoint of B
do a binary search of A[i] in B
if hit and A[i] != A[i-1], add to intersection array
increment i pointer

Soln 2 : O(mn)
loop i,j from 0
if A[i] <B[j]: increment i
if B is less than A: increment j

if A[i] == B[j] and A[i] != B[i-1]:
    Intersection Found!
    i++; j++;
    if A[i] == B[j]
    i++; j++;

soln3: Hash
loop i from 0 till len(A)-1 (n)
    add in dict - o(1)
loop i from 0 till len(B)-1(m)
    check if B[i] in dict o(1)
    if so add in output list 

o(m+n)
"""
def intersection_sorted_array_soln2(A,B):
    o =[]
    i,j = 0,0

    #soln 2
    while i<len(A) and j <len(B):
        if A[i] == B[j]:
            if i !=0 and A[i]!=A[i-1]:
                o.append(A[i])
            i += 1
            j += 1
        elif A[i]<B[j]:
            i+=1
        else:
            j+=1
    return o   

def intersection_sorted_array_soln3(A,B):
    i,j = 0,0
    o =[]
    h = dict()
    while i <len(A):
        if not h.get(A[i]):
            h[A[i]] = 1
        i+=1
    
    while j <len(B):
        if h.get(B[j]) and B[j] not in o:
            o.append(B[j])
        j+=1
    return o

            
A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]       
            
print(intersection_sorted_array_soln2(A,B))
print(intersection_sorted_array_soln3(A,B))