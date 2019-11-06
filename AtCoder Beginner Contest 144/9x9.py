import sys
input = sys.stdin.readline

#複数入力
n,m=(int(x) for x in input().split())
l=[_ for _ in range(1,10)]
if n not in l or m not in l:
    print(-1)
else :
    print(n*m)
