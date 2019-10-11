import sys
input = sys.stdin.readline

n=int(input())
x=int(input())

odd=[i for i in range(n+1) if i%2!=0]
even=[i for i in range(n+1) if i%2==0]

ans=[]
#
import time
for i in range(len(even)):
    count=0
    temp=even[i]
    while True:
        #
        print(count,temp,even[i])
        #
        time.sleep(1)
        temp=temp/2+(2**(n-1))
        count+=1
        if temp==even[i]:
            ans.append(count)
            break
print(ans)