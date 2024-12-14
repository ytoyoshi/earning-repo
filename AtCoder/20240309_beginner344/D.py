# 標準入力
T = input()
N = int(input())
bags = []
for i in range(N):
  A, *S = input().split()
  bags.append(S)

# dp[ 袋を何個目まで処理したか ][ T の接頭辞のうちどこまで一致させられたか] dp[i][j]
INF = float('inf')
dp = [[INF] * (len(T)+1) for _ in range(N+1)]

# jの値が0の時は自明にdpに0が格納される
for i in range(N+1):
  dp[i][0] = 0

for i in range(N):
  bag = bags[i]
  for x in bag:
    for j in range(len(T)+1):
      ok = True
      for k in range(len(x)):
        if(j+k>=(len(T))):
          ok = False
          break
        if(T[j+k] != x[k]):
          ok = False
          break
      # 文字が合致していたら，dpを遷移
      if(ok):
        dp[i+1][j+len(x)] = min(dp[i+1][j+len(x)], dp[i][j]+1) 
  # 行動i+1にて，どの文字も選ばないパターンもあるので，行動"i"の時のテーブルと比較して更新
  for j in range(len(T)+1):
    dp[i+1][j] = min(dp[i+1][j], dp[i][j])

ans = dp[N][len(T)]
if ans == float("inf"):
    print("-1")
else:
    print(ans)
