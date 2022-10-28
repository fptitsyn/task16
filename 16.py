from functools import *
import sys

#sys.setrecursionlimit(1000)

@lru_cache()


def f(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return f(n // 2) + 1
    return f(3 * n) + 1


c = 0
for x in range(1, 101):
    try:
        k = f(x)
        if k > 100:
            c += 1
    except:
        continue

print(c)
