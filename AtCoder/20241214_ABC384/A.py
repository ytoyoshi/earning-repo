N , c1, c2 = input().split()
S = input()

result= ""

for i in S:
    if i != c1:
        result += c2
    else:
        result += i

print(result)