def make_carpet(n):
    if n == 0:
        return "#"
    
    pre = make_carpet(n-1)
    size = len(pre)
    new_size = size * 3
    new = [["."] * new_size for _ in range(new_size)]

    for i in range(size):
        for j in range(size):
            new[i][j] = pre[i][j]
            new[i][j + size] = pre[i][j]
            new[i][j + 2 * size] = pre[i][j]
            new[i + size][j] = pre[i][j]
            new[i + size][j + 2 * size] = pre[i][j]
            new[i + 2 * size][j] = pre[i][j]
            new[i + 2 * size][j + size] = pre[i][j]
            new[i + 2 * size][j + 2 * size] = pre[i][j]

    return ["".join(row) for row in new]

N = int(input())
carpet = make_carpet(N)
for i in carpet:
    print(i)