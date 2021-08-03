"""
i/p : "Good morning"
o/p: "gninrom doog"

"""
import stack

def reverse_string(s):
    obj = stack.Stack()
    output =""
    for i in s:
        obj.push(i)

    while not obj.isempty():
        output += obj.peek()
        obj.pop()
    return output

print(reverse_string("nus gninrom doog"))

