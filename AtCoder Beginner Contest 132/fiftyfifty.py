import sys
input = sys.stdin.readline

s=input()
l=[]
count=0
for i in range(4):
    for j in range(4):
        if s[i]==s[j]:
            count+=1
    l.append(count)
    count=0

l=set(l)
if len(l)==1 and l=={2}:
    print("Yes")
else:
    print("No")