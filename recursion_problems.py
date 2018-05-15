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

#-----------------------FIBONACCI------------------------------
    
def fib_rec(n):
    if n == 1 or n == 0:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


# Instantiate Cache information
n = 10
cache = [None] * (n + 1)

def fib_dyn(n):
    if n == 0 or n == 1:
        return n
    
    if cache[n] != None:
        return cache[n]
    
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]


def fib_iter(n):
    a = 0
    b = 1
    for i in range(0,n):
        a,b =  b, a+b
    return a