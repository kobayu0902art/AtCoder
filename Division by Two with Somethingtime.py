import sys
input = sys.stdin.readline

n=int(input())
x=input()

x=int(x,2)
num=list(range(x+1))

ans=[]
#
import time
for i in num:
    if i>2**n:
        print("Break")
        break
    count=0
    temp=i%998244353

    while True:
        if temp%2!=0:
            temp=(temp-1)/2
            count+=1
            #
            #print(i,"odd",count,temp)
            #time.sleep(0.1)
            if temp==i:
                ans.append(count)
                #
                if count!=n*2:
                    print(i,count)
                    time.sleep(1)
                break
        if temp%2==0:
            temp=temp/2+2**(n-1)
            count+=1
            #
            #467310
            #print(i,"even",count,temp)
            #time.sleep(0.1)
            if temp==i:
                ans.append(count)
                #
                if count!=n*2:
                    print(i,count)
                    time.sleep(1)
                break
#
#print(ans,sum(ans))
#992,10 1985,10 2978,10 3640,6 3971,10 4964,10 5957,10 6950,10 7281,6 7943,10 8936,10 9929,10 10922,2 11915,10 12908,10 13901,10 14563,6 14894,10 15887,10  