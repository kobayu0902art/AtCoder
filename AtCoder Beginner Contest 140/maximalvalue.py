import sys
input = sys.stdin.readline

#単入力
n=int(input())

#リスト入力
b = [int(i) for i in input().split()]

a=[]
a.append(b[0])
a.append(b[0])

for i in range(2,n):
    if b[i-1]>b[i-2]:
        a.append(b[i-1])
    else:
        a.append(b[i-2])

print(a)
print(sum(a))