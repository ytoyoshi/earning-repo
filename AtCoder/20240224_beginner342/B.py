N = int(input())
P = list(map(str , input().split()))
Q = int(input())

number = []

for i in range(Q):
    A , B = input().split()
    postionA =  P.index(A)
    positonB =  P.index(B)

    if postionA > positonB:
        number.append(B)
    else :
        number.append(A)

for i in range(len(number)):
    print(number[i] )
