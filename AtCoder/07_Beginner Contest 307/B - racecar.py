N = int(input())
S = [input() for _ in range(N)]

def check(string):
    return string == string[::-1]

for i in range(N):
    for j in range(N):
        if i != j:
            result = check(S[i]+S[j])
            if result:
                print('Yes')
                exit()

print('No')