#-------------ANAGRAMS----------------
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


#--------ARRAY-PAIR-SUMS-------------------
#Given an integer array, output all the unique pairs that sum up to a specific value k.
#So the input:
#pair_sum([1,3,2,2],4)
#would return 2 pairs:
# (1,3)
# (2,2)
#Note: for testing purposes, number of pairs output instead of the actual pairs
    
def pair_sum(arr,k):
    if len(arr)<2:
        return
    
    seen = set()
    output = set()
    
    for i in arr:
        
        x = k - i
        
        if x not in seen:
            seen.add(i)
            
        else:
            output.add((min(i,x), max(i,x)))
    
    lst = list(output)
                
    return len(lst)







##-----------------STRING-COMPRESSION----------------------
#Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
#For this problem, you can falsely "compress" strings of single or double letters. For instance,
#it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
#The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

def compress(s):
    comp = ""
    
    if len(s) == 0:
        return ""
    
    if len(s) == 1:
        return s + str(1)
    c = 1
    i = 1
    while i < len(s):
        if s[i] == s[i-1]:
            c += 1
        else:
            comp += str(s[i-1]) + str(c)
            c = 1
        i+=1
    comp += str(s[i-1]) + str(c)
            
    print(comp)
    return comp
