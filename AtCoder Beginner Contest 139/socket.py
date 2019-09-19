import sys
input = sys.stdin.readline

#複数入力
a,b=(int(x) for x in input().split())
if b==1:
    print(0)
    exit(0)
c=a
ans=1
while True:
    if c>=b:
        break
    c+=(a-1)
    ans+=1
print(ans)