"""
find out if the brackets are balanced in a string
balanced brackets: 
{ }
{ } { }
( ( { [ ] } ) )

Unbalanced brackets:
( ( )
{ { { ) } ]
[ ] [ ] ] ]

"""


import stack

         
def isbalanced_bracket(s):
    brackets = {"{":"}", "[":"]","(":")"}
    obj = stack.Stack()
    s = s.replace(' ', '')

    for i in s:
        if i in "})]":
            if obj.isempty():
                return False
            if obj.peek() in brackets.keys():
                if brackets[str(obj.peek())]== i:
                    obj.pop()
                else:
                    return False
        else:
            obj.push(i)

    if not obj.isempty():
        return False
    return True
   
print(isbalanced_bracket("[][]]]"))
