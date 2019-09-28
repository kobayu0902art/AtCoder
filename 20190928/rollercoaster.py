import sys
input = sys.stdin.readline

#複数入力
n,k=(int(x) for x in input().split())

#リスト入力
h = [int(i) for i in input().split()]

print(len([i for i in h if i>= k]))