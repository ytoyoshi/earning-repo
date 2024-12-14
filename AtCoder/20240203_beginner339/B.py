H ,W ,N = map(int,input().split())

grid =  [['.' for _ in range(W)] for _ in range(H)]

# 方向の変更（上、右、下、左）
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# 現在の位置と方向
current_row, current_col = 0, 0
current_direction = 0

for _ in range(N):
    # 現在のマスの色を確認し、塗り替える
    if grid[current_row][current_col] == '.':
        grid[current_row][current_col] = '#'
        # 方向転換（時計回り）
        current_direction = (current_direction + 1) % 4
    else:
        grid[current_row][current_col] = '.'
        # 方向転換（反時計回り）
        current_direction = (current_direction - 1) % 4

    # 1マス進む
    current_col += directions[current_direction][0]
    current_row += directions[current_direction][1]

    # トーラス状に調整
    current_row = (current_row + H) % H
    current_col = (current_col + W) % W

# 最終的なグリッドを出力
for row in grid:
    print(''.join(row))