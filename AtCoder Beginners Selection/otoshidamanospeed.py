n,y=(int(x) for x in input().split())

for k in range(n+1):
    for j in range(n+1-k):
        for i in range(n+1-j-k):
            if i*10000+j*5000+k*1000 == y and i+j+k==n:
                print(i,j,k)
                exit(0)
print(-1,-1,-1)