import sys
import itertools
input = sys.stdin.readline

#単入力
n=int(input())

#リスト入力
a = [int(i) for i in input().split()]
for i,j in itertools.product(range(1,n+1), range(n)):
    if a[j]==i:
        print(j+1,end=' ')