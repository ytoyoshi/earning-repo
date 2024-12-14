N = int(input())
A = list(map(int, input().split()))
count = 0

"""Continue processing flag"""
flag = True

while flag:
    for i in range(N):
        if A[i] % 2 == 1:
            flag = False
            continue
    if flag:
        count += 1
        for i in range(N):
            A[i] = int(A[i] / 2)

print(count)
