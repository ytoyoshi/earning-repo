def get_index(A):
    from collections import defaultdict

    index_map = defaultdict(list) 
    duplicates = {}

    for i, value in enumerate(A):
        index_map[value].append(i)

    for value, indices in index_map.items():
        if len(indices) > 1:
            duplicates[value] = indices

    return duplicates

def calc_cost(list_A, W):
    total_cost = 0
    for indices in list_A.values():
        list_cost = [W[i] for i in indices]
        list_cost.sort()  
        total_cost += sum(list_cost[:-1])

    print(total_cost)

#入力
N = int(input())
A = list(map(int,input().split()))
W = list(map(int,input().split()))

A_list = get_index(A)

calc_cost(A_list, W)
