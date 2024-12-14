N, M = map(int,input().split())
shops = [input().strip() for _ in range(N)]

min_shops = N

for bit in range(1 << N):
    tastes = [0] * M
    count = 0
    for i in range(N):
        if bit & (1 << i):
            count += 1
            for j in range(M):
                if shops[i][j] == "o":
                    tastes[j] = 1
    if all(tastes):
        min_shops = min(min_shops, count)

print(min_shops)