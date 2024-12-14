N = int(input())
l = [list(input().split())for _ in range(N)]

youngest = int(l[0][1])
position = 0

for i in range(N):
    if int(l[i][1]) < youngest:
        youngest = int(l[i][1])
        position = i

l2 = []

for i in range(position,N):
    l2.append(l[i])

for i in range(position):
    l2.append(l[i])

for i in range(N):
    print(l2[i][0])
