N = int(input())

G =[]

for i in range(N):
    A_list = list(map(int,input().split()))
    G.append(A_list)

for j in range(N):
    print_list = []
    for k in range(N):
        if G[j][k] == 1:
            print_list.append(k+1)
    print(" ".join(map(str, print_list)))