N ,M = map(int,input().split())
H = list(map(int,input().split()))

hand = 0
count = 0

for i in range(N):
    hand += H[i]
    if hand > M:
        break
    count += 1

print(count)