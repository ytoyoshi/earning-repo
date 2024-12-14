S = input()

B_index = []
R_index = []
K_index = 0

for i in range(len(S)):
    if S[i] == "B":
        B_index.append(i)
    if S[i] == "R":
        R_index.append(i)
    if S[i] == "K":
        K_index = i

if (B_index[0] + B_index[1]) % 2 == 1 and R_index[0] < K_index < R_index[1]:
    print("Yes")
else: 
    print("No")
