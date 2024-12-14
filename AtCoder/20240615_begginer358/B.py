N, A = map(int,input().split())
T = list(map(int,input().split()))

time = 0

for i in range(N):
    if time <= T[i]:
        time = T[i] + A
    else :
        time += A
    print(time)