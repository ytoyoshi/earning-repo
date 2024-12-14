N = int(input())
d =[int(input()) for _ in range(N)]

d.sort(reverse=True)

kagami = [d[0]]
min_size = 0

while len(d)>0:
    min_size = d[0]
    if min_size < kagami[-1]:
        kagami.append(min_size)
    d.pop(0)

print(len(kagami))