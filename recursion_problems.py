#----------------REVERSE-STRING-USING-ONLY-RECURSION------------
def reverse(s):
    if len(s) == 0:
        return ""
    s = list(s)
    return s.pop() + reverse(s)

def reverse2(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse2(s[:-1])