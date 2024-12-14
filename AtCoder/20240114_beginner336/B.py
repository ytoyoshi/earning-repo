N = bin(int(input()))[2:]

count = 0

for i in reversed(N):
    if i == '0':
        count += 1
    else:
        break

print(count)
