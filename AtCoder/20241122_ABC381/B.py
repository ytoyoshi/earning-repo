S = input()

if len(S)%2 == 1:
    print("No")
    exit()

for i in range(0, len(S), 2):
    if i+1 >= len(S) or S[i] != S[i+1]:
        print("No")
        exit()

count = {}
for j in S:
    count[j] = count.get(j,0) + 1

for k in count.values():
    if k != 2:
        print("No")
        exit()

print("Yes")