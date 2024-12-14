import numpy as np

N = int(input())

number = str(np.base_repr(N-1,5))
result = ''

for i in str(number):
    result += str (int(i)*2)

print(int(result))