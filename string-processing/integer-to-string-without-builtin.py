"""
    Input: 123
    Output: "123"
    Input: -123
    Output: "-123"
"""
def integer_to_string(input):
    if  input< 0:
        neg = True
        input *=-1
    else:
        neg = False
    res = ""
    if input == 0:
        res = "0"
        return res
    while input>0:
        res+=(chr(ord("0") + input%10))
        input = input//10
    if neg:
        res+=(chr(ord("-")))
    return res[::-1]


print(integer_to_string(0))
print(integer_to_string(-123))