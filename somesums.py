n,a,b=(int(x) for x in input().split())
ans=0
for i in range(1, n+1):
    if a <= sum([int(c) for c in str(i)]) <= b:
        ans += i
print(ans)