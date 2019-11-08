# coding: utf-8

h,w=(int(x) for x in input().split())
n,m=(int(x) for x in input().split())
pattern=[]
for _ in range(n):
    pattern.append(input())
q=int(input())
locate=[]
for _ in range(q):
    tempx,tempy=(int(x) for x in input().split())
    locate.append((tempx-1,tempy-1))

white="_"
black="#"
line=white*w
field=[line]*h

# #and#→_ #and_→# _and#→# 
for i in range(q):
    for j in range(m):
        templ=list(field[locate[i][0]+j])
        for k in range(n):
            if pattern[j][k]==black and field[locate[i][0]+j][locate[i][1]+k]==black:
                templ[locate[i][1]+k]=white
            elif pattern[j][k]==black and field[locate[i][0]+j][locate[i][1]+k]==white:
                templ[locate[i][1]+k]=black
            elif pattern[j][k]==white and field[locate[i][0]+j][locate[i][1]+k]==black:
                templ[locate[i][1]+k]=black
        field[locate[i][0]+j]="".join(templ)
for i in range(h):
    print(field[i])