import sys
input = sys.stdin.readline
n,m=(int(x) for x in input().split())
l = [int(i) for i in input().split()]

l.sort(reverse=True)
for i in range(m):
    l[0]=l[0]//2
    l.sort(reverse=True)
total=sum(l)

print(total)
 