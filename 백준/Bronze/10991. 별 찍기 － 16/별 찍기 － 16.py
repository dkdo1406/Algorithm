N = int(input())

for i in range(1, N+1):
    print(" " * (N-i), end = "")
    for j in range(1, i+1):
        print("*", end= "")
        print(" ", end= "")
    print()