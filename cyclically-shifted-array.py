def find(A):
    l = 0
    h = len(A)-1
    while l <h:
        m = (l + h ) // 2

        if A[m]>A[h]:
            l = m+1
        elif A[m] <= A[h]:
            h = m
    return l
A = [4,5,6,7,0,1,2]
print(find (A))