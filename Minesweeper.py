import sys
input = sys.stdin.readline

h,w=(int(x) for x in input().split())

sl=[]

for _ in range(h):
    s = input()
    sl.append(s[:-1])

for i in range(h):
    for j in range(w):
        mc=0
        #print("in j:",i,j,":sl:",sl[i][j])
        if sl[i][j]!="#":
            for k in range(-1,2):
                #print("in k:",k)
                for l in range(-1,2):
                    if (i==0 and k==-1) or (j==0 and l==-1) or (i==h-1 and k==1) or (j==w-1 and l==1):
                        continue
                    #print("in l:",k,l,":sl:",sl[i+k][j+l])
                    if sl[i+k][j+l]=="#":
                        mc+=1
                        #print("mc",str(mc))
                if (i==0 and k==-1) or (j==0 and l==-1) or (i==h and k==1) or (i==w and l==1):
                        continue
        if j == 0:
            sl[i]=sl[i][j].replace('.',str(mc))+sl[i][j+1:]
        elif j == w-1:
            sl[i]=sl[i][:j]+sl[i][j].replace('.',str(mc))
        else:
            #print("else",sl[i][:j-1])
            sl[i]=sl[i][:j]+sl[i][j].replace('.',str(mc))+sl[i][j+1:]
        #print("replaced:",sl[i],"sl:",sl)

#print(sl)

for i in range(h):
    print(sl[i])