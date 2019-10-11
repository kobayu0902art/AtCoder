import sys
input = sys.stdin.readline

n=int(input())
x=input()

x=int(x,2)
num=list(range(x+1))

ans=[]
for i in num:
    if i>2**n:
        break
    count=0
    temp=i
    while True:
        if temp%2!=0:
            temp=(temp-1)/2
            count+=1
            if temp==i:
                ans.append(count)
                break
        if temp%2==0:
            temp=temp/2+2**(n-1)
            count+=1
            if temp==i:
                ans.append(count)
                break
print(sum(ans))