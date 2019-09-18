import sys
input = sys.stdin.readline

s=int(input())
l = [int(i) for i in input().split()]

count=0
for i in range(len(l)-2):
    if l[i]<l[i+1]<l[i+2]:
        count+=1
    if l[i]>l[i+1]>l[i+2]:
        count+=1

print(count)