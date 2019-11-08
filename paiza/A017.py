# coding: utf-8

h,w,n=(int(x) for x in input().split())

nextblock=[]
for _ in range(n):
    nextblock.append([int(i) for i in input().split()])

dot="."
blockunit="#"

line=dot*w
field=[line]*h

i=0

for i in range(len(nextblock)):
    for j in range(h):
        nexthight=h-1
        flag=False
        for k in range(nextblock[i][2],nextblock[i][1]+nextblock[i][2]):
            #print(k)
            if field[j][k]!=blockunit:
                pass
            else:
                nexthight=j-1
                #print("更新",nexthight)
                flag=True
                break
        if flag==True:
            break
    for l in range(nexthight-nextblock[i][0]+1,nexthight+1):
        templ=list(field[l])
        for m in range(nextblock[i][2],nextblock[i][2]+nextblock[i][1]):
            templ[m]=blockunit
        field[l]="".join(templ)
    #for ww in range(h):
        #print(field[ww])
    #print("\n")

for i in range(h):
    print(field[i])