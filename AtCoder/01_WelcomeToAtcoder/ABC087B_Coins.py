"""500yen"""
A = int(input())
"""100yen"""
B = int(input())
"""50yen"""
C = int(input())
"""sum"""
X = int(input())
count = 0

"""Full search"""
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            sum = i * 500 + j * 100 + k * 50
            if sum == X:
                count += 1

print(count)
