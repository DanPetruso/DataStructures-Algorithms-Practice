#----------------REVERSE-STRING-USING-ONLY-RECURSION------------
def reverse(s):
    if len(s) == 0:
        return ""
    s = list(s)
    return s.pop() + reverse(s)

