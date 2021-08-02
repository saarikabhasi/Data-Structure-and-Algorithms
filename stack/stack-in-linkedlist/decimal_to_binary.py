"""
convert a decimal integer to binary

example: 242 -> 11110010

"""

import stack

def decimal_to_binary(d):
    output = ""
    obj = stack.Stack()
    while d>=1:
        obj.push(d%2)   
        d = d//2
    while not obj.isempty():
        output += str(obj.peek())
        obj.pop()
    return output

print(decimal_to_binary(5))