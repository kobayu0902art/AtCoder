#入力用、先頭に絶対つける
import sys
input = sys.stdin.readline

#単入力
n=int(input())

#複数入力
n,m=(int(x) for x in input().split())

#リスト入力
l = [int(i) for i in input().split()]

#0リスト,空リスト
l=[0]*n
l=[]

#リスト要素追加
l.append(n)

#リスト重複なし
l=set(l)

#リスト大きい順ソート
l.sort(reverse=True)

#素因数分解リスト列挙
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

#偶数True奇数False
def evenjudge(obj):
    if obj %2==0:
        return True
    else:
        return False

#2重ループ
import itertools
for i,j in itertools.product(range(n), range(n)):
    pass

#リスト内組み合わせ
import itertools
itertools.combinations(list,n)