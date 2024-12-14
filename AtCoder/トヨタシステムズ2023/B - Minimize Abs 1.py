def find_X(A, L, R):
    result = []

    for i in range(len(A)):
        # L 以上 R 以下の整数 X を求める
        X = max(L, min(R, A[i]))

        # Y について条件を満たす X を計算
        Y1 = A[i] - abs(L - A[i])
        Y2 = A[i] + abs(R - A[i])

        if abs(X - A[i]) <= abs(Y1 - A[i]) and abs(X - A[i]) <= abs(Y2 - A[i]):
            result.append(X)
        else:
            result.append(Y1) if abs(Y1 - A[i]) <= abs(Y2 - A[i]) else result.append(Y2)
    
    return result

N ,L ,R = map(int,input().split())
A = list(map(int,input().split()))

result = find_X(A, L, R)
print(" ".join(map(str, result)))
