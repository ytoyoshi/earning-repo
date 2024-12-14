N = int(input())
A = list(map(int,input().split()))

check = True
count = 0

while check:
    for i in range(N):
        if A[i]%2 == 0:
            A[i] = A[i]/2
        else:
            check = False
            break
    if check == True: 
        count += 1  

print(count)
    