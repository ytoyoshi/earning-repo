N = int(input())
G = [[] for _ in range(N)]

for _ in range (N-1):
    a, b = map(int, input().split())
    a, b = a - 1 , b - 1
    G[a].append(b)
    G[b].append(a)

def dfs(s):   
    dist = [-1] * N
    dist[s] = 0

    # スタックでdfs
    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist [v] + 1
    
    return dist

# 頂点0から
dist0 = dfs(0)
mv = max(enumerate(dist0), key=)