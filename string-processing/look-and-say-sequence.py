"""
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211
To generate a member of the sequence from the previous member, 
read off the digits of the previous member and
record the count of the number of digits in groups of the same digit.

For example, 1 is read off as one 1 which implies that the count of 1 is one. 
As 1 is read off as "one 1", the next sequence will be written as 11 where 1 replaces one.
Now 11 is read off as "two 1s" as the count of "1" is two in this term. 
Hence, the next term in the sequence becomes 21.

"""
def look_and_say_seq(s):
    n = len(s)
    i = 0 
    result = []
    while i<n:
        count = 1
        if i+1<len(s) and s[i+1] == s[i]:
            i+=1
            count+=1
        result.append(str(count)+s[i])
        i+=1
    return ''.join(result)

s = "1"
print(s)
n = 4
for i in range(n-1):
    s = look_and_say_seq(s)
    print(s)

