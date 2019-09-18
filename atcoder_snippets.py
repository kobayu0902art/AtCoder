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