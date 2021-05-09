"""

[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
o/p = 3  (return index of first occurence)

"""

def find_dup(a,t):
    l = 0
    h = len(a)-1
    while l<=h:

        m = (l+h)//2

        if a[m]>t:
            h = m -1
        elif a[m]<t:
            l = m+1
        else:
            if m-1<0:
                return m
            if a[m-1] != t:
                return m
            h = m-1

    return -1
    

print(find_dup([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401],28))