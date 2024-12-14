N = input()
kardList = list(map(int, input().split()))

aliceKardList = []
bobKardList = []

for i in range(len(kardList)):
    if i % 2 == 0:
        aliceKardList.append(max(kardList))
        kardList.remove(max(kardList))
    else:
        bobKardList.append(max(kardList))
        kardList.remove(max(kardList))

print(sum(aliceKardList) - sum(bobKardList))
