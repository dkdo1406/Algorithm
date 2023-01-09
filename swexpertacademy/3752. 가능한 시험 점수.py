T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [0 for _ in range(sum(arr)+1)]
    visited[0] = 1
    q = [0]
    for i in arr:
        for j in range(len(q)):
            if visited[i + q[j]] == 0:
                visited[i + q[j]] = 1
                q.append(i+q[j])

    answer = len(q)

    print("#{0} {1}".format(test_case, answer))