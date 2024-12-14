N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

total = 0
p = 0

for i in range(N):
    if A[i] >= B[p]:
        total += A[i]
        p += 1
        if p == M:
            print(total)
            exit()
print(-1)
