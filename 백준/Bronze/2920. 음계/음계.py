S = list(map(int, input().split()))

ascending = [i for i in range(1, 9)]
descending = sorted(ascending, reverse= True)
if S == ascending:
    print("ascending")
elif S == descending:
    print("descending")
else:
    print("mixed")
