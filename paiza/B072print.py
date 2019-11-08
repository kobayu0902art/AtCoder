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
            print(j,k,locate[i][0]+j,locate[i][1]+k)
            if pattern[k][j]==black and field[locate[i][0]+k][locate[i][1]+j]==black:
                print("黒黒")#,"\n")
                templ[locate[i][1]+k]=white
                temps="".join(templ)
                print(temps,"\n")
            elif pattern[k][j]==black and field[locate[i][0]+k][locate[i][1]+j]==white:
                print("白黒")#,"\n")
                templ[locate[i][1]+k]=black
                temps="".join(templ)
                print(temps,"\n")
            elif pattern[k][j]==white and field[locate[i][0]+k][locate[i][1]+j]==black:
                print("黒白")#,"\n")
                templ[locate[i][1]+k]=black
                temps="".join(templ)
                print(temps,"\n")
        field[locate[i][0]+k]="".join(templ)
    print("\n")
    for i in range(h):
        print(field[i])
print("\n")
for i in range(h):
    print(field[i])