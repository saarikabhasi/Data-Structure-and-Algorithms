def find_upper_case(str,ind):
    # find if string has upper case letter
    if str[ind].isupper():
        return str[ind]
    elif ind == len(str) - 1:
        return "No upper letter found"
    else:
        return find_upper_case(str,ind+1)
print("upper case letter", find_upper_case("lucidprogramminf",0))

def string_length(str):
    # calculate length of string
    if str == "":
        return 0
    else:
        return 1+string_length(str[1:])
print("string length", string_length("luci fjs"))

def find_consonant(str):
    # find letter in str othe than a, e, i , o u
    if str == "":
        return 0
    else:
        if str[0].lower() not in "aeiou" and str[0].isalpha():
            return  1 + find_consonant(str[1:])
        return 0 + find_consonant(str[1:])
        

print(" No of consonents", find_consonant("js"))

def recursive_multiply(x,y):
    if x < y :
        return recursive_multiply(y,x)
    if y==0:
        return 0
    else:
        return x + recursive_multiply(x,y-1)
     

print("multiply with recursion 2*3",recursive_multiply(2,0))