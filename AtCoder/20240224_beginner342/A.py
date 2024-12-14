S = input()

x = S[0]
y = S[1]
z = S[2]

if x!=y and x==z:
    print(2)
    exit()
elif x!=y and y==z:
    print(1)
    exit()
else :
    count = 1
    for i in range(len(S)):
        if x != S[i]:
            print(count)
            exit()
        count += 1