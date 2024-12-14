N = int(input())
A = list(map(int,input().split()))

count = 0

for i in range(N):
    first_index = A.index(i+1)
    second_index = A.index(i+1,first_index+1)
    
    if second_index - first_index == 2:
        count += 1

print(count)