dist = [0, 3, 4, 8, 9, 14,23]
point= 'ABCDEFG'

p,q= input().split()

point_p = point.find(p)
point_q = point.find(q)

print(abs(dist[point_p]-dist[point_q]))