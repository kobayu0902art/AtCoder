import sys
import itertools
input = sys.stdin.readline

def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

n=int(input())

l=factorize(n)
print(l)
if len(l)==1:
    print(n-1)
    exit()

if len(l)==2:
    print(l[0]+l[1]-2)
    exit()

while True:
    l.sort(reverse=True)
    temp=l[-1]*l[-2]
    print("temp:",l)
    l.pop()
    l.pop()
    print("pop: ",l)
    l.append(temp)
    print("app: ",l)
    if len(l)==2:
        break
print(l)
print(l[0]+l[1]-2)
