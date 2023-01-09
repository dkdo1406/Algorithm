#우선순위 : 좌우의 구슬차가 적을수록, 많을수록, 합이 클수록, 왼쪽부터 순서대로일수록

#가운데 구슬은 무조건 0이다.
# 균형을 맞추는 경우의 수는 2가지가 있는데 가운데 구슬이 있거가 없는 경우이다.

marbles = [5,5,1,4]


# 모든 경우의 수를 1부터 전체를 다 넣은것까지 만든다.
# 그리고 배열의 수가 홀수일 때와 짝수일 때 2가지 버전으로 만들어 조건에 맞을 경우 정답배열에 넣고 마지막 경우의수까지 비교한다.

def permu(prefix, k, r):
    if len(prefix) == r:
        yield prefix
    else:
        for i in range(k, len(marbles)):
            marbles[i], marbles[k] = marbles[k], marbles[i]
            for next in permu(prefix + [marbles[k]], k + 1, r):
                yield next
            marbles[i], marbles[k] = marbles[k], marbles[i]

def checkBeautiful(arr):
    # 무조건 가운데를 기준으로 같을경우에만 ture 리턴
    if len(arr) % 2 == 0:
        if sum(arr[:len(arr)//2 ]) == sum(arr[len(arr)//2:]):
            return True
    else:
        if sum(arr[:len(arr) // 2]) == sum(arr[len(arr) // 2 + 1:]):
            return True
    return False
def checkPriority(a, b):
    # 둘 중 합이 큰걸 우선으로 한다.
    # 그냥 총합이 아니라 홀수일때와 짝수일 때 2가지로 나눠서 한다.
    print(a, b)
    if sum(a[:len(a) // 2]) > sum(b[:len(b) // 2]):
        return a
    elif sum(a[:len(a) // 2]) < sum(b[:len(b) // 2]):
        return b
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        if a[i] < b[i]:
            return a
        elif a[i] > b[i]:
            return b
    return

answer = []
for r in range(len(marbles), 0, -1):
    for permutation in permu([], 0, r):
        if checkBeautiful(permutation):
            # 조건에 맞으니 우선순위를 보고 앞에 것과 비교한다.
            # 여기 들어온것들은 일단 우선순위 1을 무조건 만족한다.
            if answer == []:
                answer = permutation
            else:
                if answer == permutation:
                    continue
                answer = checkPriority(answer, permutation)
    if len(answer) > 0:
        break
print(answer)