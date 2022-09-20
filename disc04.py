def count_stair_ways(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n,k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    return sum(count_k(n-i,k) for i in range(1,k+1))

def even_weighted(s):
    return [i*s[i] for i in range(0,len(s)) if i%2 == 0]

x=[1,2,3,4,5,6]

def max_product(s):
    if len(s) == 0:
        return 1
    else:
        return max(s[i] * max_product(s[i+2:]) for i in range(0,len(s)))

y = [5,10,5,10,5,1,2]