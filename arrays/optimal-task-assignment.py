"""
Assign tasks to workers so that the time it takes to complete all the tasks is minimized 
given a count of workers and an array where each element indicates the duration of a task.

[6, 3, 2, 7, 5, 5]
(2+7) = 9
(5+5) =  10
(3+6) = 9
max([2,7], [5,5], [3,6]) = 10 
So we need totally 10 hours to finish all tasks

Algorithm:
Greedy algorithm:
1. Sort array in increasing order
2. Pair first and last number
3. Add and return max


"""

def optimal_task_assigment(A):

    A = sorted(A)
    m = 0
    for i in range(len(A)//2):
        s = A[i]+A[~i]
        m = max(m,s)
    return m

print(optimal_task_assigment([0, 0, 2, 7, 5]))
