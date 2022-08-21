"""还没检查过这份答案"""
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    m,n = max(m,n),min(m,n)
    if n == 1:
        return m
    else:
        return m + multiply(m,n-1)



def rec(x, y):
    if y > 0:
        return x * rec(x, y - 1)
    return 1
rec(3, 2)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print (n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(n*3+1)


def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    m = min(n1%10,n2%10,1)
    if min(n1,n2) == 0:
        return max(n1,n2)
    elif n1%10 <= n2%10:
        return n1%10 + 10**m*merge(n1//10,n2)
    else:
        return n2%10 + 10**m*merge(n1,n2//10)



def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """

    def repeat(n):
        assert n > 0,'n must be an  integer greater than 0'
        if n == 1:
           return f(x)

        else:

           return f(repeat(n-1))

    return repeat




def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(k):
        if n>k>1 and n%k ==0 or k == 1:
            return False
        elif k == 2:
            return True
        else:
            return prime_helper(k-1)
    return prime_helper(n)


