def keep_ints(cond,n):
    assert n>0 and n%1==0,'n must be a positive integer'
    i=1
    while i<=n:
        if cond(i):
            print (i)
        i+=1
    return 

def make_keeper(n):
    def check(cond):
        i=1
        while i<=n:
            if cond(i):
                print (i)
            i+=1
        return
    return check

def curry2(h):
    return lambda x:lambda y:h(x,y)
"""curry2=lambda h:lambda x:lambda y:h(x,y)"""

def print_delayed(x):
    def delay_print(y):
        print (x)
        return print_delayed(y)
    return delay_print

def print_n(n):
    def inner_print(x):
        if n<=0:
            print ("done")
        else:
            print (x)
        return print_n(n-1)
    return inner_print