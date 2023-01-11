def solution(strings, n):
    arr = []
    for i in strings:
        arr.append(list(i))
    arr.sort()
    arr.sort(key = lambda x: x[n])
    answer = []
    for i in arr:
        answer.append(''.join(i))
    return answer