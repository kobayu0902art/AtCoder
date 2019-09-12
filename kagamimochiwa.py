n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

l.sort(reverse=True)
flag=True
while flag:
    for i in range(len(l)-1):
        if l[i]==l[i-1]:
            del l[i]
        if i == len(l)-1:
            flag=False
print(len(l))