"""
"rail safety" = "fairy tales"
"roast beef" = "eat for BSE"
"William Shakespeare" = "I am a weakish speller"
"Madam Curie" = "Radium came"
"""

def anagram_check(s1, s2):
    hash = dict()
    i = 0
    j = 0
    if len(s1)!=len(s2):
        return False
    while i<len(s1):
        if s1[i].isalpha():
            if s1[i] in hash: 
                hash[s1[i].lower()]+=1
            else:
                hash[s1[i].lower()]=1
        i+=1
    print(hash)
    while j < len(s2):
        if s2[j].isalpha():
            if s2[j].lower() in hash:
                hash[s2[j].lower()]-=1
            else:
                hash[s2[j]] = 1

        j+=1
    print(hash)
    for i in hash:
        if hash[i] !=0:
            return False
    return True

s1 = "Live on time, emit no e"
s2 = "Live on time, emit no e"
print(anagram_check(s1,s2))



