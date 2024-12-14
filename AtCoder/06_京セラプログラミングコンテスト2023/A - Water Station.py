    N = int(input())

    x = N % 5

    if x==0:
        print(N)
    elif x <= 2:
        print(N-x)
    else:
        print(N-x+5)