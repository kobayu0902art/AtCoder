a,b=(int(x) for x in input().split())

s=input()
c=0
if s[0]=="1":
    c+=1
if s[1]=="1":
    c+=1
if s[2]=="1":
    c+=1
print(c)


n=int(input())
count=0
l=input()
l=l.split()
for i in range(n):
    l[i]=int(l[i])
def evenjudge(obj):
    if obj %2!=0:
        return 0
    else:
        return 1
flag=True
while flag:
    j=0
    for i in range(n):
        j+=evenjudge(l[i])
    if j==n:
        for i in range(n):
            l[i]=l[i]/2
        count+=1
    else:
        flag=False
print(count)