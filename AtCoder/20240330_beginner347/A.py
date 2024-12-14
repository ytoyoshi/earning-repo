N ,K = map(int,input().split())
A = list(map(int,input().split()))

l = []

for i in A:
    if i%K == 0:
        l.append(i//K)

print(" ".join(map(str, sorted(l)))) 