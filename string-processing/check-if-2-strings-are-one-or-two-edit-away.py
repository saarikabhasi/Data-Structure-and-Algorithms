"""
Check if given two strings are one edit or zero edit away.

Example:
pale, ple -> true

"""


def one_or_zero_edits_away_approach_1(s1,s2):
    length_difference = abs(len(s1)-len(s2))
    if length_difference>1:
        # if difference is greater than 1, two strings are more than 1 edit away
        return False
    # both strings have same length or has one extra letter

    smallest_string = s1 if len(s1)<len(s2) else s2
    largest_string = s2 if len(s2)>len(s1) else s1
    
    found_difference = 1
    
    s_index = 0
    l_index = 0


    while s_index<len(smallest_string) and l_index <len(largest_string):
        print(found_difference)
        if smallest_string[s_index] != largest_string[l_index]:
            #first difference found
            if found_difference > 1:
                return False
            found_difference +=1

            if length_difference != 0:
                l_index+=1
                continue
        
        s_index+=1
        l_index+=1

    
    print(length_difference,l_index)
    if length_difference == 1 and l_index<=len(largest_string)-1:
        return False
    return True



print(one_or_zero_edits_away_approach_1("ple","pales"))