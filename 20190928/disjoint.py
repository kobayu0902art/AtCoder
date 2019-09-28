import sys
input = sys.stdin.readline

#複数入力
a,b=(int(x) for x in input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

ad=make_divisors(a)
bd=make_divisors(b)

cd=set(ad)&set(bd)

print(ad,bd,cd)