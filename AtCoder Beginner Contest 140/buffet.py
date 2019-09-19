import sys
input = sys.stdin.readline

#単入力
n=int(input())

#リスト入力
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]


for i in range(1,n):
    if a[i]-a[i-1]==1:
        b.append(c[a[i]-2])
print(sum(b))