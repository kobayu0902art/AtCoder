import sys
input = sys.stdin.readline

#単入力
n=int(input())

l=[]
for i in range(n):
    l.append(input()[:-1])

for i in range(n):
    if l[i][-1]=="s" or l[i][-2:]=="sh" or l[i][-2:]=="ch" or l[i][-1]=="o" or l[i][-1]=="x":
        l[i]=l[i]+"es"
    elif l[i][-1]=="f":
        l[i]=l[i][:-1]
        l[i]=l[i]+"ves"
    elif l[i][-2:]=="fe":
        l[i]=l[i][:-2]
        l[i]=l[i]+"ves"
    elif l[i][-1]=="y" and l[i][-2] not in ("a","i","u","e","o"):
        l[i]=l[i][:-1]
        l[i]=l[i]+"ies"
    else:
        l[i]=l[i]+"s"
    print(l[i])
