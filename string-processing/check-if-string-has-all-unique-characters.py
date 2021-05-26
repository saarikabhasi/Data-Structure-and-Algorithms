"""
Given a string, check if all the characters in string is unique. 

1. Using binary search: (not implemented)
    * sort the string 
    * search if each string occurs once. 

    Time complexity: O(nlogn)
    Space complexity: Extra space to store sorted string

2. Hashtable (implemented)
    * Time complexity: O(n)
    * Space: O(n) ,since we need to store string number of occurence in a map or dictionary

3. Reduce space by a factor of eight by using a bit vector. Assumes all the characters are lower case

    

"""
def is_unique(s):
    s = s.lower()
    s = s.replace(" ", '')
    d = dict()

    for i in s:
        
        if i in d:
            return False
        else:
            d[i] = 1
    return True
    

def is_unique_bit(s):
    checker = 0
    for i in s:
        val = ord(i)-ord('a')
        if ( (checker & (1<<val)) >0):
            return False
        checker |= (1 << val)
    return True 

print(is_unique('AbCDefG'))
print(is_unique_bit("abcdc"))