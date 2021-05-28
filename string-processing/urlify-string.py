"""
URLify :
Write a method to replace all the spaces in a string with "%20". 
You may assume that the string has sufficient space at the end to hold the additional characters and that you are given the "true" length of the string.

Example:
Input: "Mr John Smith    ", 13
Output: Mr%20John%20Smith

Approach:

1. Brute force approach: (Not implemented)
    1. Create new arraylist
    2. Loop from 0 till end of input
    3. Keep pushing character to the new arraylist
    4. When a space is hit in input, stop pushing but go to next loop and set a spaceflag to True
    5. if another character is found, then Add the string '%20' (per character) to the arraylist 
        6. if flag was true, push the current character to the arraylist,set flag to false
    7. if character was not found exit.

Complexity:
    Time: O(len(s))
    Space: additional space to store new arraylist

2. Try reducing space complexity by adding %20 inplace (implemented)
    

"""

def Urlify(s,truelength):
    #truelength is the real length of the string
    space_count = len(s)-truelength
    st = list(s)
    for q in range(truelength-1,0,-1):
        if space_count >=0:
            if st[q] == " ":
                #space
                st[q+space_count]="0"
                st[q+(space_count-1)]="2"
                st[q+(space_count-2)] ="%"
                space_count -=2

            else:
                st[q+space_count] = st[q]
    s ="".join(st)
    print(s)

Urlify("Mr John Smith    ", 13)
Urlify('ab cd ef    ',8)
