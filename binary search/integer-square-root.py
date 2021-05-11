"""
Write a function that takes a non-negative integer, k, 
and returns the largest integer whose square is less than or 
equal to the specified integer k.

"""




def integer_square_root(k):
    l = 1
    h = k

    while l<=h:
        m = (l + h) // 2
        if l == m or h == m :
            if l**2 < k:
                return l 
            if h **2 <k:
                return h
        if m**2 == k:
            return m
        elif m**2 > k:
            h = m
        else:
            if m**2 < k:
                l = m
        
            






print(integer_square_root(16))