T = int(input())

for test_case in range(1, T + 1):
    answer = "no"
    a, b = list(input().split())
    if a == b:
        answer = "yes"
    else:
        a = a * 101
        b = b * 101
        if a[:100] == b[:100]:
            answer = "yes"
    print(f"#{test_case} {answer}")
