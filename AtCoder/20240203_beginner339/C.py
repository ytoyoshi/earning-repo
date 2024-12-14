N = int(input())
A = list(map(int, input().split()))

# 初期の乗客数
passengers = 0

# 各停車ごとに乗客数の変化を計算
for change in A:
    passengers += change
    passengers = max(passengers, 0)

# 最終的な乗客数を出力
print(passengers)
