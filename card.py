n=input()
l = [int(i) for i in input().split()]

l.sort(reverse=True)
alice=0
bob=0

while len(l) != 0:
    alice+=int(l[0])
    del l[0]
    if len(l) == 0:
        break
    bob+=int(l[0])
    del l[0]

print(alice-bob)