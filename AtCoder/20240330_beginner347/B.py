def count_substrings(S):
    substrings = set()
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            substrings.add(S[i:j])
    return len(substrings)

def main():
    S = input().strip()  # 入力文字列を受け取る
    result = count_substrings(S)  # 部分文字列の数を計算する
    print(result)

if __name__ == "__main__":
    main()
