N = int(input())
S = input()
Q = int(input())

""" 
計算量が多い回答
for _ in range(Q):
    c, d = map(str,input().split())
    S = S.replace(c,d)
"""
from string import ascii_lowercase

from_str = ascii_lowercase
to_str = ascii_lowercase

for _ in range(Q):
    c, d = input().split()
    to_str = to_str.replace(c,d)

print(S.translate(str.maketrans(from_str,to_str))) 