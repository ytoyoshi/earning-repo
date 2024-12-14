N = int(input())
l = [int(input())for _ in range(N)]

count = 1
mini = min(l)
l.remove(min(l))

while len(l):
    for i in range(N):
        if len(l) ==0:
            break
        if mini < min(l):
            mini = min(l)
            l.remove(min(l))
            count += 1
        elif mini == min(l):
            l.remove(min(l))

print(count)
