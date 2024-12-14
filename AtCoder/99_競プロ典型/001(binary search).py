# N:切れ目の数
# L:ようかんのサイズ
# K:選ぶ切れ目の数
# A:切れ目の位置

N ,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

# 全ての長さをx以上にできるか
def check(x):
    num = 0 #何個切れたか
    pre = 0 #前回の切れ目

    for i in range(N):
        if A[i] - pre >= x:
            num += 1
            pre = A[i]

    # 最後の切れ端の計算。X以上なら加算。
    if L - pre >= x:
        num += 1
    
    return (num >= K + 1)

# 二分探索
left, right = -1, L + 1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)