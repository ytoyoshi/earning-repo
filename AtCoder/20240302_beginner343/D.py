from collections import defaultdict

def count_score_variety(N, T, updates):
    scores = [0] * N  # 初期得点は全員0点
    score_counts = defaultdict(int)  # 得点の出現回数を記録する辞書

    # 各得点を記録
    for i in range(T):
        player, increase = updates[i]
        scores[player - 1] += increase
        score_counts[scores[player - 1]] += 1
    
    # 各時点での得点の種類数を数える
    result = []
    for i in range(T):
        player, increase = updates[i]
        score = scores[player - 1]
        unique_scores = len(score_counts)
        if score_counts[score] == 1:  # もし現在の得点が1回しか出現していない場合
            unique_scores += 1
        result.append(unique_scores)
    return result

# 入力を受け取る
N, T = map(int, input().split())
updates = [list(map(int, input().split())) for _ in range(T)]

# 各時点での得点の種類数を計算して出力
result = count_score_variety(N, T, updates)
for r in result:
    print(r)
