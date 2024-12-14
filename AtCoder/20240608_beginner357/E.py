def count_result(N, a):
    graph = [[] for _ in range(N + 1)]
    for u in range(1, N + 1):
        graph[u].append(a[u - 1])
    
    result = [False] * (N + 1)
    
    def dfs(u):
        if result[u] is not False:
            return result[u]
        result[u] = []
        stack = [u]
        ok_list = [False] * (N + 1)
        while stack:
            node = stack.pop()
            if not ok_list[node]:
                ok_list[node] = True
                result[u].append(node)
                for v in graph[node]:
                    if not ok_list[v]:
                        stack.append(v)
        return result[u]
    
    for i in range(1, N + 1):
        result[i] = dfs(i)
    
    count = 0
    for u in range(1, N + 1):
        count += len(result[u])
    
    return count

N = int(input())
a = list(map(int,input().split()))

print(count_result(N, a)) 
