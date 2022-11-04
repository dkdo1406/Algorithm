def solution(n):
    jumpList = [0 for _ in range(2002)]
    jumpList[1] = 1
    jumpList[2] = 2
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(3, n+1):
        jumpList[i] = jumpList[i-1] + jumpList[i-2]
    return jumpList[n] % 1234567