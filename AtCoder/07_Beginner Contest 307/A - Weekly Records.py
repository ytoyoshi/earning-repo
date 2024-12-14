N = int(input())
A = list(map(int,input().split()))

week = 0

for i in range(N):
    a = 0 
    for j in range(week,week+7):
        a += A[j]
    print(a)
    week += 7