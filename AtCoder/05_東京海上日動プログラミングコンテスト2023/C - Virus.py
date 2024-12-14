import collections

def distinct(p1, p2):
    dx, dy = p1[0] - p2[0], p1[1] - p2[1]
    return dx * dx + dy * dy

N, D = map(int, input().split())
# タプルの方がパフォーマンスが良いらしい
l = [tuple(map(int, input().split())) for _ in range(N)]

virus = [False for _ in range(N)]

# 一人目が感染
virus[0] = True

# 感染者の位置を格納するキュー
q = collections.deque()
q.append(0)

while len(q):
    # 感染者の位置を取得。キューが０件の場合、感染が増えないと判断してループ終了
    x = q.popleft()
    for i in range(N):
            if virus[i] == False and distinct(l[i], l[x]) <= D * D:
                virus[i] = True
                #　感染者の位置をキューに追加
                q.append(i)

for i in range(N):
    if virus[i]:
        print("Yes")
    else:
        print("No")
