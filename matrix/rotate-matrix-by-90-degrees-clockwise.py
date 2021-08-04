"""
input:
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]

output:
    [13,9,5,1],
    [14,10,6,2],
    [15,11,7,3],
    [16,12,8,4]

0 3 1
_______________
0 3 0
_______________
0 3 -1
_______________
0 3 -2
_______________
1 2 1
_______________
1 2 0
_______________
1 2 -1
_______________
"""

def rotate_by_90_clockwise(a):
    n = len(a)
    
    for layer in range(0,n //2):
        first = layer
        last = n-1-layer
        for i in range(layer,n):
            offset = n-1-i-first
            print(first,last,offset)
            temp = a[layer][i]
            a[layer][i] = a[last-offset-i][i]
            a[last-offset-i][i] = a[last][last-i]
            a[last-i][last-i] = a[layer][last]
            a[layer][last] = temp
            print("_______________")
    
    return A

        

A = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]

print(rotate_by_90_clockwise(A))
