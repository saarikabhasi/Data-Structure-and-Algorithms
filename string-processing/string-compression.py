"""
input :aaabaaaaccaaaaba
output: a3b1a4c2a4b1a1

input:abc
output:abc

input:abcaaa
output:abca3
"""
 

def string_compression_recursion(s,p,q,o):
    q = p+1
    checker = s[p]
    count = 1
    o += checker
    if q == len(s) and count > 1:
        o +=str(count)
    while q <len(s):
        if s[q] == checker:
            count+=1
            q+=1
            if q == len(s):
                o +=str(count)
        else:
            if count > 1:
                o += str(count)
 
            return string_compression_recursion(s,q,q,o)

    return o


def string_compression_recursion_inplace(s,p,q):
    if p<len(s):
        q = p+1
       
        checker = s[p]
        count = 1
        if q == len(s) and count > 1:
            s = s[:p+1] + str(count) +s[q:]
        while q <len(s):
            if s[q] == checker:
                count+=1
                q+=1
                if q == len(s):
                    s = s[:p+1] + str(count) +s[q:]
            else:
                if count > 1:
                    s = s[:p+1] + str(count) +s[q:]
                    q = p+2
                p = q
                
                return string_compression_recursion_inplace(s,p,q)

    return s
print(string_compression_recursion_inplace("aaabaaaaccaaaaba",0,0))
