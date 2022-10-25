

def memory(n):
    """
    >>> f=memory(10)
    >>> f(lambda x:x*2)
    20
    >>> f(lambda x:x-7)
    13
    >>> f(lambda x:x>5)
    True
    """
    def f(g):
        nonlocal n
        n=g(n)
        return n
    return f

def mystery(p,q):
    """
    p=[2,3]
    q=[4,[p]]
    mystery(q,p)
    """
    p[1].extend(q)
    q.append(p[1:])

def group_by(s,fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for e in s:
        key = fn(e)
        if key in grouped:
            grouped[key].append(e)
        else:
            grouped[key] = [e]
    return grouped

def add_this_many(x,el,s):
    copy = s[:]
    for i in copy:
        if i == x:
            s.append(el)

def filter(iterable,fn):
    for i in iterable:
        if fn(i):
            yield i

def merge(a,b):
    A=next(a)
    B=next(b)
    while True:
        if A == B:
            yield A
            A=next(a)
            B=next(b)
        elif A > B:
            yield B
            B=next(b)
        else:
            yield A
            A=next(a)
    

