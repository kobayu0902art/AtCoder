import sys
input = sys.stdin.readline

n,x=(int(x) for x in input().split())

count=0
temp=x
while True:
    if temp%2!=0:
        print(count,":",temp,"odd")
        #1ひいて半分
        #1ひく=いちばんうしろの1を0にしてそれよりうしろを1に→末尾0になる
        #半分=いっこ右にずらす
        temp=(temp-1)/2
        count+=1
        if temp==x:
            print(count,":",temp,"odd")
            break
    if temp%2==0:
        print(count,":",temp,"even")
        #半分=いっこ右にずらす→いちばん先頭が0になる
        #n桁目に1足す 00→01もしくは01→10
        temp=temp/2+2**(n-1)
        count+=1
        if temp==x:
            print(count,":",temp,"even")
            break