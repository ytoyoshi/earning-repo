number = []

while True:
    try:
        A = int(input())
        number.append(A)
    except Exception:
        break

for i in reversed(number):
    print(i)