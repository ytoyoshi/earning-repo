N, S = map(int, input().split())
A = list(map(int, input().split()))
A2 = A + A

# 尺取り法で区間和がSとなる部分を探す
right = 0
current_sum = 0
A1_sum = sum(A)  # 1周期の合計

for left in range(N):
    # rightを進める（current_sumがSを超えても少し先まで確認）
    while right < 2*N and current_sum <= S:
        if current_sum == S:  # 現在の区間和がSに等しい場合
            print("Yes")
            exit()
            
        # 周期性を利用した判定
        if current_sum < S and A1_sum > 0:
            remaining = S - current_sum
            if remaining % A1_sum == 0 and remaining // A1_sum >= 0:
                print("Yes")
                exit()
                
        current_sum += A2[right]
        right += 1
    
    # 最後のチェック
    if current_sum == S:
        print("Yes")
        exit()
    
    # 周期性を利用した最後のチェック
    if current_sum < S and A1_sum > 0:
        remaining = S - current_sum
        if remaining % A1_sum == 0 and remaining // A1_sum >= 0:
            print("Yes")
            exit()
            
    # leftを進める前に、除外される値を引く
    current_sum -= A2[left]
    if right == left + 1:  # rightが進められなかった場合の調整
        right = left + 1
        current_sum += A2[left]

print("No")