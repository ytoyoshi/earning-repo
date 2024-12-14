N, M = map(int,input().split())

table = [[False]* N for _ in range(N)]

for i in range(M):
    A = list(map(int,input().split()))
    for j in range(len(A) - 1):
        a = A[j]
        b = A[j + 1]
        table[a - 1][b - 1] = True
        table[b - 1][a - 1] = True

count = 0

for i in range(N):
    for j in range(N):
        now = table[i][j]
        if now == False:
            count += 1

print((count - N) // 2)