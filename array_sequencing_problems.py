#Given two strings, check to see if they are anagrams. 
#An anagram is when the two strings can be written using the exact same 
#letters (so you can just rearrange the letters to get a different phrase or word).
#For example:
#"public relations" is an anagram of "crap built on lies."
#"clint eastwood" is an anagram of "old west action"
#Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

def anagram(s1,s2):
    s1 = list(s1.lower().replace(" ", ""))
    s2 = list(s2.lower().replace(" ", ""))
    
    check = {}
    
    for i in s1:
        if i in check:
            check[i] += 1
        else:
            check[i] = 1
            
    for i in s2:
        if i in check:
            check[i] -= 1
        else:
            return False
        
    for i in check:
        if check[i] != 0:
            return False
        
    return True