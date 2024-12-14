import heapq

heap = [5,4,10,2,5]


heapq.heapify(heap)

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

print(heap)