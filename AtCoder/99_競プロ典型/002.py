from itertools import product

N = int(input())

if N % 2 == 1 :
    exit()

def isvalid(S) :
    score = 0

    for i in S:
        if i == '(':
            score += 1
        elif i == ')':
            score -= 1
        
        if score < 0:
            return False
        
    return (score == 0)

for S in product(['(',')'],repeat = N):
    if isvalid(S):
        print(*S,sep='')