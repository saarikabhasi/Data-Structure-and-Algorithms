def issubstring(concatented_string,s2):
    p = 0
    q = 0
    flag = False
    while p<len(concatented_string):

        if q == len(s2):
            return True
        if concatented_string[p] == s2[q]:
            q+=1
            flag = True
        else:
            q = 0
            flag = False
        p+=1
    
    return flag
def string_rotation(s1,s2):
    return issubstring(s1+s1,s2)

print(string_rotation('waterbottle','erbottlewat'))
print(string_rotation('ABCD','ADCB'))