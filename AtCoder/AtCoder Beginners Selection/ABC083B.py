def calc(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

N, A, B = map(int,input().split())

count = 0

for i in range(1,N+1):
    number = calc(i)
    if A <=  number <= B:
        count += i

print(count)