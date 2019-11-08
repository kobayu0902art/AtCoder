# coding: utf-8
p = [int(i) for i in input().split()]
k=p.pop(-1)
p.sort()
ansl=[]
flag=False
if k>64:
    tempk=64
else:
    tempk=k
for i in range(tempk):
    for j in range(tempk):
        for l in range(tempk):
            ansl.append((p[0]**l)*(p[1]**j)*(p[2]**i))
ansl=set(ansl)
ansl=list(ansl)
ansl.sort()
print(ansl[k-1])