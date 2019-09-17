n,k,q=(int(x) for x in input().split())
a=[]
for i in range(q):
    a.append(int(input()))
p=[0]*n
for i in range(k):
    for j in range(n):
        p[j]+=1
for i in range(n):
    for j in range(q):
        p[i]-=1
        if a[j]-1 == i:
            p[i]+=1


for i in range(n):
    if p[i]>0:
        print("Yes")
    else:
        print("No")
