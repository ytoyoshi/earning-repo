N = int(input())
S = input()

first = (1+N)//2-1 
midle = (1+N)//2
end = (1+N)//2+1

if N==1 and S =="/":
    print("Yes")
    exit()

if N%2==0:
    print("No")
    exit()

for i in range(first):
    if "1" not in S[i]:
        print("No")
        exit()

if "/" not in S[midle-1]:
    print("No")
    exit()

for i in range(midle,end):
    if "2" not in S[i]:
        print("No")
        exit()

print("Yes")