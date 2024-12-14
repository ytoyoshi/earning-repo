N = int(input())
A = list(map(int,input().split()))

alice = 0
bob = 0

aliceTurn = True

A.sort()

for i in range(N):
    if aliceTurn:
        alice += A[-1]
        A.pop()
        aliceTurn = False
    else:
        bob += A[-1]
        A.pop()
        aliceTurn = True

print(alice-bob)