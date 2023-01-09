from collections import deque

answer = 0

def bfs(numbers, target, sum, index):
    global answer
    q = deque([(sum, index)])
    while q:
        sum, number = q.popleft()
        if sum == target and number == len(numbers):
            answer += 1
        elif sum != target and number == len(numbers):
            pass
        else:
            q.append((sum + numbers[number], number + 1))
            q.append((sum - numbers[number], number + 1))

def solution(numbers, target):
    bfs(numbers, target, 0, 0)

    return answer
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers,target))