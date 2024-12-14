N,A,B = map(int,input().split())

allList = []
sumList = []

for i in range(N+1):
    allList.append(i)

for k in allList:
    ketaSum = 0
    for j in range(len(str(abs(k)))):
        ketaSum = ketaSum + int(str(abs(k))[j])
    if ketaSum >= A and ketaSum <= B:
        sumList.append(k)

print(sum(sumList))

