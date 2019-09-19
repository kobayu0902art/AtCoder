import sys
input = sys.stdin.readline

#単入力
n=int(input())

#リスト入力
h = [int(i) for i in input().split()]
ans=0
l=[]
for i in range(n):
    if h[i]>h[i-1]:
        l.append(ans)
        ans=0
    elif h[i]<=h[i-1]:
        ans+=1
    if i ==0:
        ans=0
l.append(ans)
print(max(l))