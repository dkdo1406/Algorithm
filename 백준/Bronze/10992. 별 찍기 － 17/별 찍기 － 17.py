N = int(input())

for i in range(1, N+1):
    print(" " * (N-i), end= "")
    if i == 1:
        print("*")
    elif i == N:
        print("*" * ((i * 2) - 1))
    else:
        print("*", end= "")
        print(" " * (((i-1) * 2) - 1), end= "")
        print("*")

