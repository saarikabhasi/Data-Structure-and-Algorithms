"""
find if given sentence or word is palindrome. 
Sentence/word may have non alphanumeric characters too.
"""

def palindrome_check(sentence):
    i = 0
    j = len(sentence)-1
    while i < j :
        if not sentence[i].isalnum() and i<j:
            i+=1
        if not sentence[j].isalnum() and i<j:
            j-=1

        if sentence[i].lower() != sentence[j].lower():
            return False


        i+=1
        j-=1
    return True

print(palindrome_check("Live on time, emit no evil."))