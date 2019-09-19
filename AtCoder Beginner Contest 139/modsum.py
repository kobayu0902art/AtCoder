import sys
input = sys.stdin.readline

#単入力
n=int(input())
n/=10000
l=[i for i in range(1,n+1)]

#ll=l
#ans=0
#for i in range(len(l)):
#    if i==n-1:
#        break
#    ans+=ll[i]%l[i+1]
#    #if i==0:
#        #del ans[0]

#print(ans*10000)