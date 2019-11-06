import sys
import numpy as np
from numpy import linalg as LA

input = sys.stdin.readline

a,b,x=(int(_) for _ in input().split())

#a/2,x/a**2*b

u = np.array([a,0])
v = np.array([a,b-x/(a**2)])

i = np.inner(u, v)
n = LA.norm(u) * LA.norm(v)

c = i / n
ans = np.rad2deg(np.arccos(c))

print(ans)
