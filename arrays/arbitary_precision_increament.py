"""
Given: An array of non-negative digits that represent a decimal integer.

Problem: Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.

1. 1,4,9
    +1
result: 1, 5, 0

2. 9,9,9
    +1
result: 1,0,0,0

"""

def arbitary_precision_increment(A,increment):

    n = len(A)
    A[-1] = A[-1] + increment
    q = 0
    for i in range(n-1,-1,-1):
        if q>=1:
            A[i]=A[i]+q

        r = A[i] % 10
        q = A[i] // 10
        A[i] = r
    if q >=1:
        A.insert(0,q)

    print(A)



A=[1,4,9]
arbitary_precision_increment(A,-1)
arbitary_precision_increment(A,1)
A=[1,0,0,0]
arbitary_precision_increment(A,10)