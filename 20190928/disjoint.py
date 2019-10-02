import sys
import itertools
input = sys.stdin.readline

#複数入力
a,b=(int(x) for x in input().split())

def factorize(n):
    b = 2
    #本当は[]
    fct = [1]
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

print(len((set(factorize(a))&set(factorize(b)))))