"""
Problem:
Is it possible to advance from the start of the array to the last element 
given that the maximum you can advance from a position is based on the value 
of the array at the index you are currently present on?

Example:
    3, 3, 1, 0, 2, 0 ,1

Condition: 
Array of positive integers

Winnable scenerio: Can reach end of array
step 1: p at a[0], a[0]= 3
    p can be moved 0 to 3 steps inclusively
    Lets say p is moved 1 step
step 2: p at a[1], a[1]= 3
    p can be moved 0 to 3 steps inclusively
    Lets say p is moved 3 steps
step 3: p at a[4], a[4]= 2
    p can be moved 0 to 2 steps inclusively
    Lets say p is moved 2 steps
step 4: p at a[6]. 
    
    P WON

Non winnable: Not reaching end of array
Greedy approach:
    step 1: p at a[0], a[0]= 3
        Lets say p is moved 3 step
    step 2: p at a[3], a[3]= 0
        p can not move anywhere 

        P LOST
Non greedy approach:
    step 1: p at a[0], a[0]= 3
        Lets say p is moved 2 step
    step 2: p at a[2], a[2]= 1
        if p is moved 1 step:
            p is stuck at a[3]
        else if p is move 0 step
            p is stuck at a[2]
        
        Either way p can not reach a[6]
        Hence, P LOST

Some arrays will always be non winnable
Example:
3, 2, 0, 0, 2, 0, 1

Algorithm:
The algorithm should say if the given array is winnable by any approach or not winnable at all.

Suppose n is size of array
1. Loop from 0 till n-1 and maximum_reached_index = 0 
2. Beginning a loop check if i>maximum_reached_index
    * if true return False
3. maximum_reached_index = max(maximum_reached_index,i+A[i])

4. When i = n-1. Return True

"""
def array_advance_game(A):
    i = 0 
    n =len(A)
    maximum_reached_index = 0
    while i<n:
        if i>maximum_reached_index:
            return False
        if i == n-1:
            return True
        maximum_reached_index = max(maximum_reached_index,i+A[i])
        i += 1

A = [3, 2, 0, 0, 2, 0, 1] 
print(array_advance_game(A))

B = [3, 3, 1, 0, 2, 0 ,1]
print(array_advance_game(B))

C =[2, 4, 1, 1, 0, 2, 3]   
print(array_advance_game(C))