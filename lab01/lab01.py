from operator import sub
from turtle import Turtle


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    assert k>=0 and k%1==0,'k must be a non-negative integer'
    y = 1
    while k > 0:
        y = y*n
        n,k = n-1,k-1
    return y


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    assert y>=0 and y%1==0,'y must be a non-negative integer'
    sum = 0
    while y > 0:
        sum = sum + y % 10
        y = y // 10
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"

    """想尝试将小数也纳入domain中，取n=8.0808080808时返回结果是True，
    I tried to envolve decimal numbers but I failed,here is the code:

    def double_eights(n):
	Left=n//1
	Right=n-L
	while Left>=88 or Right*10%1>0:
        if (Left-88)%100==0 or int(Right*100)==88:#错在小数的乘法上
            return True
        else:
            Left=Left//10
            Right=sub(Right*10,int(Right*10))
        return False
    return False"""
    assert n%1==0,'n must be an integer'
    n = abs(n)
    while n>=88:
        if (n-88)%100==0:
            return True
        else:
            n=n//10
    return False


