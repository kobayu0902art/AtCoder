import sys
input = sys.stdin.readline

#単入力
n=int(input())

def evenjudge(obj):
    if obj %2!=0:
        return False
    else:
        return True

if evenjudge(n)== True:
    print(0.5)
else:
    print(((n+1)/2)/n)