S = int(input())

def main():
    result = []
    for x in range(S+1):
        for y in range(S+1):
            for z in range(S+1):
                if x + y + z <= S:
                    result.append((x,y,z))
    return result

result = main()
for i in result:
    print(*i)