from itertools import product

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))

Q = int(input())
X = list(map(int,input().split()))

sums = set()
for a, b, c in product(A, B, C):
    sums.add(a + b + c)

for query in X:
    if query in sums:
        print("Yes")
    else:
        print("No")