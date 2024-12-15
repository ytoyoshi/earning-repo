from itertools import combinations
from collections import OrderedDict

N = list(map(int,input().split()))

values = dict(zip(['A','B','C','D','E'],N))

result = {}

for i in range(1,len(values)+1):
    for j in combinations('ABCDE', i):
        key_str = ''.join(j)
        total = sum(values[k] for k in j)

        if total not in result:
            result[total] = []
        result[total].append(key_str)

sorted_totals = sorted(result.keys(), reverse=True)
    
final_result = []
for total in sorted_totals:
    sorted_combinations = sorted(result[total])
    final_result.extend(sorted_combinations)

for i in final_result:
    print(i)