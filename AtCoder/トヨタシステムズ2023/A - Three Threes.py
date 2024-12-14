def calculate_diagonal_length(vertex1, vertex2):
    # 正五角形の各頂点に対応する座標を定義
    vertices = {'A': (0, 0), 'B': (1, 0), 'C': (0.5, 0.5*(5**0.5)),
                'D': (-0.5, 0.5*(5**0.5)), 'E': (-1, 0)}

    # 2点間の距離を計算
    distance = ((vertices[vertex1][0] - vertices[vertex2][0])**2 +
                (vertices[vertex1][1] - vertices[vertex2][1])**2)**0.5

    return distance

def main():
    # 入力
    input_str1 = input()
    input_str2 = input()

    s1, s2, t1, t2 = input_str1[0], input_str1[1], input_str2[0], input_str2[1]

    # 対角線の長さを計算
    diagonal_length_s = calculate_diagonal_length(s1, s2)
    diagonal_length_t = calculate_diagonal_length(t1, t2)

    # 結果の表示
    if (diagonal_length_s == diagonal_length_t or
            diagonal_length_s == calculate_diagonal_length(s1, t2) or
            diagonal_length_s == calculate_diagonal_length(s2, t1) or
            calculate_diagonal_length(s1, s2) == diagonal_length_t or
            calculate_diagonal_length(s2, t1) == diagonal_length_t or
            calculate_diagonal_length(t1, t2) == diagonal_length_s):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
