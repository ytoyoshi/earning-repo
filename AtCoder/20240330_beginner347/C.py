N ,A ,B = map(int,input().split())
D = list(map(int,input().split()))

if D[0] < A:
    for i in D:
        day_after = i % (A + B)
        if not 1 <= day_after <= A:
            print("No")
            exit()
else :
    for i in D:
        day_after = i % (A + B)
        if day_after == 0:
            continue
        if not 1 <= day_after <= A:
            print("No")
            exit()

print("Yes")
