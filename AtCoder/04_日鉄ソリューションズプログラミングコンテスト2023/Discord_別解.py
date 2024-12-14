N,M=map(int,input().split())
G=[{j for j in range(i+1,N)} for i in range(N-1)]

for _ in range(M):
    lis=list(map(lambda x:int(x)-1,input().split()))
    for i in range(N-1):
        a=min(lis[i],lis[i+1])
        b=max(lis[i],lis[i+1])
        if b in G[a]:G[a].remove(b)
ans=0
for i in range(N-1):
    ans+=len(G[i])
print(ans)