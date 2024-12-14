N, D= map(int,input().split())
T = list(map(int,input().split()))

s = -1

for i in range(1,N):
    if T[i]-T[i-1]<=D:
        s = T[i]
        break

print(s)
