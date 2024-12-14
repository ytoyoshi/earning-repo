H, W = map(int, input().split())
room = [input() for _ in range(H)]

new_room = []

T = "TT"
PC = "PC"

for i in range(H):
    table = room[i]
    while True:
        if table.find(T) != -1:
            table = table.replace(T, PC, 1)
        else:
            new_room.append(table)
            break

for i in range(len(new_room)):
    print(new_room[i])