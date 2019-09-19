n,k,q=(int(x) for x in input().split())
a=[]
for i in range(q):
    a.append(int(input()))
p=[k-q]*n

for i in range(q):
    p[a[0]-1]+=1
    del a[0]
for i in range(n):
    if p[i]>0:
        print("Yes")
    else:
        print("No")
