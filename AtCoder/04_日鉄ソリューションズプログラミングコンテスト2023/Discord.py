N, M = map(int, input().split())
list = [list(map(int, input().split())) for _ in range(M)]

count = 0
# 数字ごとに隣り合うを調べる
for i in range(1, N + 1):
    # 隣り合う数字を登録する集合
    nearSet = set()
    for j in range(M):
        for k in range(N):
            if k == 0 and list[j][k] == i:
                nearSet.add(list[j][k + 1])
            elif k == N - 1 and list[j][k] == i:
                nearSet.add(list[j][k - 1])
            elif k != 0 and list[j][k] == i:
                nearSet.add(list[j][k - 1])
                nearSet.add(list[j][k + 1])
    # 集合内に数字が含まれない場合、カウント
    for j in range(1,N+1):
        if i != j and (j not in nearSet):
            count += 1

print(count // 2)
