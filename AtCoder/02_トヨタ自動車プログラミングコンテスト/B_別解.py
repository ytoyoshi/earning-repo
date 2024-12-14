# HとWはグリッドの高さと幅
H, W = map(int, input().split())

# boxは各セルに含まれる文字を格納するリスト
box = []
for i in range(H):
    # 入力された行を読み込む
    letter = input()
    box.append(letter)
ß
# directionは8つの可能な方向を示す（右、左、上、下、右上、右下、左上、左下）
direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

# wordは見つけるべき単語
word = "snuke"

# グリッドをループする
for i in range(H):
    for j in range(W):
        # 現在のセルが's'で始まる場合、8つの方向に単語を検索開始
        if box[i][j] == "s":
            for d in range(8):
                # move_i, move_jは現在調査中のセルの位置
                move_i = i
                move_j = j
                # ansは単語の文字が見つかったセルのリスト
                ans = []
                for k in range(5):
                    # 位置が範囲内であり、かつ該当のセルに検索中の文字がある場合
                    if (
                        0 <= move_i < H
                        and 0 <= move_j < W
                        and box[move_i][move_j] == word[k]
                    ):
                        # そのセルの位置をリストに追加
                        ans.append([move_i, move_j])
                        # 次のセルへ移動
                        move_i += direction[d][0]
                        move_j += direction[d][1]
                    else:
                        # 条件が満たされない場合はループを中断
                        break

                # 'snuke'のすべての文字が見つかった場合
                if len(ans) == 5:
                    # 各文字の位置を表示
                    for l in range(5):
                        print(ans[l][0] + 1, ans[l][1] + 1)
