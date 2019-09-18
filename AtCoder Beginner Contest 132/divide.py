import sys
input = sys.stdin.readline

n=int(input())
l = [int(i) for i in input().split()]
l.sort()
i=n//2
print(l[i]-l[i-1])