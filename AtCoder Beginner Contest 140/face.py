import sys
input = sys.stdin.readline


#複数入力
n,k=(int(x) for x in input().split())

#単入力
s=input()
ll=[]
for j in range(k):
    ss=s
    for l in range(n):
        for r in range(l,n+1):
            print("l:r",l,r)
            print("ss",ss, end='')
            slr = ''.join(list(reversed(ss[l:r])))
            print("slr",slr)
            slr=slr.replace('L', 'X').replace('R', 'L').replace('X', 'R')
            print("replaced slr",slr)
            ss=ss[:l]+slr+ss[r:]
            print("ss",ss)
            happy=0
            for i in range(n+1):
                if not(i==0 and ss[i]=="L") or not(i==n and ss[i]=="R"):
                    if ss[i]=="L" and ss[i-1]=="L":
                        happy+=1
                    elif ss[i]=="R" and ss[i+1]=="R":
                        happy+=1

            ll.append(happy)
print("len(ll)",len(ll))
print("ll",ll)
print(max(ll))