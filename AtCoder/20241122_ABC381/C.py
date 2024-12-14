N = input()
S = input()

ans = 1

for i in range(len(S)):
    if S[i] == '/':
        L ,R = i-1,i+1
        length = 1
        while(L >= 0 and R < len(S)) and (S[L] == '1' and  S[R] == '2'):
            length += 2
            L -= 1
            R += 1
            if length > ans:
                ans = length

print(ans)