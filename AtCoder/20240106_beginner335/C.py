N, Q = map(int,input().split())
# 逆順のリストを生成。リストの後ろの追加のみで、削除は実施しない。
dragon = [(i, 0) for i in range(N, 0, -1)]
x, y = 1, 0

for _ in range(Q):
    # クエリの入力
    T, C = input().split()
    if T  == "1":
        if C == "R":
            x += 1
        elif C == "L":
            x -= 1
        elif C == "U":
            y += 1
        elif C == "D":
            y -= 1
        dragon.append((x, y))
    else:
        print(*dragon[-int(C)])