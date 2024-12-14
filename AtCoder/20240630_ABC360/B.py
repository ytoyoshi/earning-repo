def check(S, T):
    len_S = len(S)
    len_T = len(T)

    for w in range(1, len_S + 1):
        if len_S % w == 0:
            parts = [S[i:i + w] for i in range(0, len_S, w)]
            concatenated = ''.join(parts[i] for i in range(len(parts)) if i < len_T)
            if concatenated == T:
                return "Yes"
    return "No"

S, T = input().split()
print(check(S, T))
