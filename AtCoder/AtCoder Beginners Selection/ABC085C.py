N, Y = map(int,input().split())

for i in range(N+1):
    for j in range(N+1-i):
            num = N - (i+j)
            if i*10000+j*5000+num*1000 == Y:
                print(f"{i} {j} {num}")
                exit()
print("-1 -1 -1")
            
