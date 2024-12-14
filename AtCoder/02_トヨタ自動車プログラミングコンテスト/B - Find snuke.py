H, W = map(int, input().split())
list = [input() for _ in range(H)]

searchWord = "snuke"

"""1文字目を見つけて全方向に総当たりで詮索してみる"""
for i in range(H):
    for j in range(W):
        if list[i][j] == searchWord[0]:
            """上方向への詮索"""
            if (
                i >= len(searchWord) - 1
                and list[i - 1][j] == searchWord[1]
                and list[i - 2][j] == searchWord[2]
                and list[i - 3][j] == searchWord[3]
                and list[i - 4][j] == searchWord[4]
            ):
                print("{} {}".format(i, j))
                print("{} {}".format(i - 1, j))
                print("{} {}".format(i - 2, j))
                print("{} {}".format(i - 3, j))
                print("{} {}".format(i - 4, j))
            """右上方向への詮索"""
            if (
                i >= len(searchWord) - 1
                and j <= W - len(searchWord)
                and list[i - 1][j + 1] == searchWord[1]
                and list[i - 2][j + 2] == searchWord[2]
                and list[i - 3][j + 3] == searchWord[3]
                and list[i - 4][j + 4] == searchWord[4]
            ):
                print("{} {}".format(i, j))
                print("{} {}".format(i - 1, j + 1))
                print("{} {}".format(i - 2, j + 2))
                print("{} {}".format(i - 3, j + 3))
                print("{} {}".format(i - 4, j + 4))
            """右方向への詮索"""
            if (
                j <= W - len(searchWord)
                and list[i][j + 1] == searchWord[1]
                and list[i][j + 2] == searchWord[2]
                and list[i][j + 3] == searchWord[3]
                and list[i][j + 4] == searchWord[4]
            ):
                print("{} {}".format(i, j))
                print("{} {}".format(i, j + 1))
                print("{} {}".format(i, j + 2))
                print("{} {}".format(i, j + 3))
                print("{} {}".format(i, j + 4))
            """右下方向への詮索"""
            if (
                i <= H - len(searchWord)
                and j <= W - len(searchWord)
                and list[i + 1][j + 1] == searchWord[1]
                and list[i + 2][j + 2] == searchWord[2]
                and list[i + 3][j + 3] == searchWord[3]
                and list[i + 4][j + 4] == searchWord[4]
            ):
                print("{} {}".format(i, j))
                print("{} {}".format(i + 1, j + 1))
                print("{} {}".format(i + 2, j + 2))
                print("{} {}".format(i + 3, j + 3))
                print("{} {}".format(i + 4, j + 4))
            """下方向への詮索"""
            if (
                i <= H - len(searchWord)
                and list[i + 1][j] == searchWord[1]
                and list[i + 2][j] == searchWord[2]
                and list[i + 3][j] == searchWord[3]
                and list[i + 4][j] == searchWord[4]
            ):
                print("{} {}".format(i, j))
                print("{} {}".format(i + 1, j))
                print("{} {}".format(i + 2, j))
                print("{} {}".format(i + 3, j))
                print("{} {}".format(i + 4, j))
            """左下方向への詮索"""
            if (
                i <= H - len(searchWord)
                and j >= len(searchWord) - 1
                and list[i + 1][j - 1] == searchWord[1]
                and list[i + 2][j - 2] == searchWord[2]
                and list[i + 3][j - 3] == searchWord[3]
                and list[i + 4][j - 4] == searchWord[4]
            ):
                print("{} {}".format(i, j))
                print("{} {}".format(i + 1, j - 1))
                print("{} {}".format(i + 2, j - 2))
                print("{} {}".format(i + 3, j - 3))
                print("{} {}".format(i + 4, j - 4))
            """左方向への詮索"""
            if (
                j >= len(searchWord) - 1
                and list[i][j - 1] == searchWord[1]
                and list[i][j - 2] == searchWord[2]
                and list[i][j - 3] == searchWord[3]
                and list[i][j - 4] == searchWord[4]
            ):
                print("{} {}".format(i, j))
                print("{} {}".format(i, j - 1))
                print("{} {}".format(i, j - 2))
                print("{} {}".format(i, j - 3))
                print("{} {}".format(i, j - 4))
            """左上方向への詮索"""
            if (
                i >= len(searchWord) - 1
                and j >= len(searchWord) - 1
                and list[i - 1][j - 1] == searchWord[1]
                and list[i - 2][j - 2] == searchWord[2]
                and list[i - 3][j - 3] == searchWord[3]
                and list[i - 4][j - 4] == searchWord[4]
            ):
                print("{} {}".format(i, j))
                print("{} {}".format(i - 1, j - 1))
                print("{} {}".format(i - 2, j - 2))
                print("{} {}".format(i - 3, j - 3))
                print("{} {}".format(i - 4, j - 4))
