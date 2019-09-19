import sys
input = sys.stdin.readline

#単入力
s=input()

#単入力
t=input()
ans=0
for i in range(3):
    if s[i]==t[i]:
        ans+=1
print(ans)