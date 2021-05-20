def check_if_one_string_is_palindrome_of_other(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) !=len(s2):
        return False
    d = dict()

    for i in s1:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1

    for i in s2:
        if i in d:
            d[i]-=1
        else:
            return False
    return True
print(check_if_one_string_is_palindrome_of_other("google","ooggle"))
print(check_if_one_string_is_palindrome_of_other("not","top"))