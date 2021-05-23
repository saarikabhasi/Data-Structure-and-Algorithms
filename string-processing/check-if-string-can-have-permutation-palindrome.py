"""

A string that has even number of length must have even number of character count and

A string that has odd number of length must have exactly one character count odd.

in other words, A set of characters can form a palidrome if atmost one character occurs odd num of times.
Example:
 tacocat
 t-2 a-2 c-2 o-1
 len - 7

"""

def check_palindrome_permutation(s):
    s = s.lower()
    s = s.replace(" ", "")
    
    d = dict()  


    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1


    odd_count = 0
    for k,v in d.items():
        if v%2 !=0 and odd_count == 0:
            odd_count +=1
        elif v%2 != 0 and odd_count !=0:
            return False
    return True
   
def hash_table(d,key):
    if key in d:
        d[key]+=1
    else:
        d[key] = 1

def check_palindrome_solution2(s):
    print(s)
    p = 0 
    q = len(s)-1
    d = dict()
    while p<=q: 
        if s[p] !=" " :
            hash_table(d,s[p])
        if s[q] != " ":
            hash_table(d,s[q])
        p +=1
        q -=1
    print(d)
    odd =0 
    for i in d: 
        if d[i]%2!=0:
            odd +=1
        if odd >1:
            return False
    return True


print(check_palindrome_permutation("Taco ct"))
print(check_palindrome_solution2("aba"))
    
