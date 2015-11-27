def love_meet(a, b):
    i = set(a)
    j = set(b)
    return(i & j)


def affair_meet(a, b, c):
    i = set(a)
    j = set(b)
    k = set(c)
    l = j & k
    m = l - i
    return(m)
