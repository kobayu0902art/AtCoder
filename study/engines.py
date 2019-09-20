import sys
input = sys.stdin.readline

#単入力
n=int(input())
pp=[]
mp=[]
pm=[]
mm=[]
zp=[]
zm=[]
pz=[]
mz=[]
for i in range(n):
    #複数入力
    a,b=(int(x) for x in input().split())
    tup=[a,b]
    if a<0 and b<0:
        mm.append(tup)
    elif a<0 and b>0:
        mp.append(tup)
    elif a>0 and b>0:
        pp.append(tup)
    elif a>0 and b<0:
        pm.append(tup)
    elif a==0 and b<0:
        zm.append(tup)
    elif a==0 and b>0:
        zp.append(tup)
    elif a>0 and b==0:
        pz.append(tup)
    elif a<0 and b==0:
        mz.append(tup)

print(pp,mp,pm,mm,zp,zm,pz,mz)