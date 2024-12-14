import math

A, B = map(int, input().split())
count = 0

if A % B == 0:
    count = A // B
else:
    count = (A // B+1)

print(count)
